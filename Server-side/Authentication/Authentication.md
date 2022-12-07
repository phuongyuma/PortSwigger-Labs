
Tool: Burp Suite
# Vulnerabilities in password-based login
## Username enumeration
#### Username enumeration via different responses

Mục đích của bài lab này là tìm ra **username** thông qua việc xem các responses khác nhau, khi ta nhập **username** đúng, repsonses được trả về sẽ khác khi ta nhập sai.

Các bước:
- Bật BurpSuite, ở tab **Proxy**, bật **Intercept** và mở truy cập link lab bằng browser của BurpSuite
- Login với username và password ngẫu nhiên, sau đó dùng tool Burp Intruder, gửi request tới **Intruder** (Sent to Intruder)
![[Pasted image 20221201165245.png]]
- Chọn vị trí chạy payload: Click **Clear §**, sau đó chọn **Add §** ở vị trí username, chỉnh url target là https://0a8300ea04551316c103d28400290033.web-security-academy.net/login
- Ở tab payload, ta thêm list **Candidate usernames** vào và nhấn **Start Attack**
- Ta xem các kết quả thì có 1 response (username=announcements) có length khác với những response khác, xem thì thấy là **Invalid password**, khác với những response khác là **Invalid username** => username là **announcements**
 ![[Pasted image 20221201174000.png]]
- Giờ login lại với username là vagrant, nhưng giờ dùng **Add §** ở vị trí passwords, asu đó thêm list **Candidate passwords** vào paypload rồi nhấn **Start attack** 
![[Pasted image 20221201175002.png]]
- Ta thấy so với những repsonse khác đều có "Incorrect password", repsonse của gói request với passwords "abc123" có **response code HTTP** là 302, nghĩa là trang web đang chuyển hướng tới địa chỉ mới. Ta thử login lại với tài khoản**announcements/abc123** thì thành công

![[Pasted image 20221201175138.png]]

#### Username enumeration via subtly different responses

Mục tiêu: Ở bài lab này chúng ta sẽ brute force username và password, sau đó từ xác định username và password thật qua các responses

Ở bài lab trước (Username enumeration via different responses), ta có thể so sánh các  độ dài của response để tìm ra username/password thật, vậy nếu các response trả về đều có độ dài khác nhau/ giống nhau thì sẽ không thể dùng phương pháp trên, vậy ta cần 


![[Pasted image 20221202092745.png]]

- Từ kết quả có được, ta có một thông báo khác biệt so với những thông báo còn lại
khi username=affiliate
![[Pasted image 20221202092450.png]]

- Lặp lại với những đổi vị trí payload thành **password**, ta thấy tại vị trí password=joshua, ta có response http code là 302
![[Pasted image 20221202093430.png]]

=>Username/ password là : affiliate/joshua
![[Pasted image 20221202093552.png]]

#### Username enumeration via response timing

Mục tiêu: 

Khi dùng cách như những câu trước, ta bị chặn 30 phút sao mới login được
=> phải tìm cách nào đó để không bị chặn
Ta search google (bypass IP-based brute-force protection with manipulating HTTP request headers.) thì có kết quả là thêm [**X-Forwarded-For**](https://en.wikipedia.org/wiki/X-Forwarded-For)
Vậy ta mỗi lần tiến hành gửi request, ta cần thay đổi X-Forwarded-For để để tránh bị block IP
![[Pasted image 20221202094215.png]]

![[Pasted image 20221202094733.png]]
Ta thêm **X-Forwarded-For**
![[Pasted image 20221202211846.png]]


Ta lọc theo thời gian phản hồi thì thấy có một response phản hồi lâu hơn hẳn những response khác (username=ftp)
![[Pasted image 20221202215551.png]]

ta thêm username khả nghi là **ftp** vào vị trí username, sau đó brute force một lần nữa nhưng lần này đặt vị trí payload ở **X-Forwarded-For** và **password**



![[Pasted image 20221202215652.png]]
![[Pasted image 20221202215819.png]]

Vậy username/ password là auto/1234


## Flawed brute-force protection
### Broken brute-force protection, IP block

Mục tiêu: Lợi dụng thiếu sót trong phòng chống brute force để brute-force mật khẩu của victim

NOTE:
- 2 cách thông thường nhất trong việc ngăn chặn brute-force:
	+ Khóa tài khoản của người dùng nếu nhập sai quá nhiều
	+ Chặn IP người dùng nếu họ đăng nhập liên tiếp quá nhiều lần
=> Nếu bộ đếm tự reset lại sau số lần khi IP đăng nhập thành công thì sau khi đăng nhập sai vài lần, kẻ tấn công có thể đăng nhập tài khoản của mình để tránh bị đạt tới ngưỡng bị block


Vậy với bài này, khi brute-force bằng **Brup Suite**, ta chèn username/ password được cho vào payload để mỗi khi sai vài lần thì ta login thành công 1 lần, tránh trường hợp bị khóa tài khoản hoặc block IP
Ta sẽ viết 1 đoạn script để tạo payload nhét vào burp suite

**payload cho username**
``` code
#create_user_payload.py
d = open('D:\CMC\Web Application Security\Portswigger\Authentication\payload_user.txt', 'w')

c = 0

while c <= 100:

    d.write("carlos\n")

    d.write("wiener\n")

    c = c + 1
```

**payload cho passwords**
``` code
#create_pass_payload.py
a = open("D:\CMC\Web Application Security\Portswigger\Authentication\candidate_pass.txt", "r")

b = open("D:\CMC\Web Application Security\Portswigger\Authentication\payload_pass.txt", "w")

length = 0

for i in a:

    b.write(i)

    b.write("peter\n")

    length = length + 1
```

Kết quả là ta được 2 file 
**payload_user.txt**  
![[Pasted image 20221203135007.png]]
**payload_pass.txt**
![[Pasted image 20221203134954.png]]

Kế tiếp ta sẽ dùng Burp Intruder để brute-force với 2 payload này
Sử dụng attack type là **Pitchfork**, chọn vị trí payload ở username và password, thêm 2 payload vào ở tab **Payloads**.
Ở tab **Resource pool**, chọn **Maxium concurrent requests** là 1 để các request được gởi đi theo đúng thứ tự từng cái một
![[Pasted image 20221203193333.png]]

Sau khi có kết quả, ta lọc với từ khóa carlos và status 3xx thì được username/ password là carlos/ chelsea

![[Pasted image 20221203193510.png]]

## Account locking
#### Username enumeration via account lock

Mục tiêu: brute-force tài khoản người dùng (lab này khóa tài khoản nếu 1 tài khoản đăng nhập sai nhiều lần)

Ta sẽ thử từng username với vài lần lặp lại cho đến khi xuất hiện thông báo khóa tài khoản, khi xuất hiện thông báo này thì có nghĩa là username của chúng ta vừa chọn là username tồn tại, sau đó chỉ cần brute-force password với username này là được

Sau khi gửi request tới Intruder, ta chọn Attack type là **Cluseter bomb**, kiểu này sẽ cho chúng ta burte-force với từng payload một, nghĩa là các payload sẽ được lần lượt thay vào.

![[Pasted image 20221203200106.png]]
Sau khi thêm payload cho username, ta thêm 5 payload null vào.
![[Pasted image 20221203200049.png]]
Khi chạy thì ta thấy có một response có độ dài khác với những response khác. Nó có thông báo lỗi **too many login attempts** => **ads** là username tồn tại
![[Pasted image 20221203200024.png]]
Thay username=ads vào request, ta thực hiện tấn công lần nữa với attack type là **sniper** và thêm payload vào vị trí password
Ta thấy tại đây không có thông báo lỗi giống những response khác => password là **monitor**
![[Pasted image 20221203202355.png]]
Thử login với tài khoản **ads/ monitor** thì ta thành công
![[Pasted image 20221203201012.png]]




# Vulnerabilities in multi-factor authentication

Xác thực 2 yếu tố tùy chọn và bắt buộc dựa trên **something you know** and **something you have**. Phương pháp này thường yêu cầu người dùng nhập một mật khẩu bình thường và một mã xác thực từ thiết bị vật lý mà họ sở hữu.

#### 2FA simple bypass

Với phương pháp xác thực 2 yếu tố thì sau khi ta nhập tên đăng nhập và mật khẩu thì sẽ xuất hiện một cái trang để nhập mã xác thực, cách đơn giản nhất để vượt qua chính là bỏ qua trang xác thực này, trực tiếp đi tới trang chính sau khi login thành công

![[Pasted image 20221204142328.png]]

Ta nhận thấy sau khi nhập mã xác thực từ email thì ta được chuyển hướng tới trang **/my-account**. Nên khi login bằng tài khoản victim mà khoản có mã xác  thực, ta sẽ thử sửa url thành **/my-account** thì thấy thành công vào được tài khoản của nạn nhân
![[Pasted image 20221204142636.png]]

#### 2FA broken logic

I will use **Burp suite** to see how 2FA of this lab works.
First, I use the credentials **wiener:peter** login to the web and input the verification code provided  on **Email client**
I go to **HTTP history**, and can see pages **/login, /login2, /academyLabHeader** have "**Cookie:  verify=wiener**", this field is used to verify who accessed to page.
And page **/login2** is used to request server generated 2FA code for user on **Email client**
![[Pasted image 20221207094702.png]]
So, I sent **POST /login2** to **Burp Intruder** and change the **verify** parameter to **carlos**, set the payload position at the **mfa-code** to burte-force the verification code
![[Pasted image 20221207101312.png]]
I find out the verification code is 1728
![[Pasted image 20221207101700.png]]
Show the response in browser and complete the lab

![[Pasted image 20221207102003.png]]