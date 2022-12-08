
Tool: Burp Suite
# Vulnerabilities in password-based login


#### 2FA broken logic

I will use **Burp suite** to see how 2FA of this lab works.
First, I use the credentials **wiener:peter** login to the web and input the verification code provided  on **Email client**
I go to **HTTP history**, and can see pages **/login, /login2, /academyLabHeader** have "**Cookie:  verify=wiener**", this field is used to verify who accessed to page.
And page **/login2** is used to request server generated 2FA code for user on **Email client**
![](../../Img_note/Pasted%20image%2020221207094702.png)

So, I sent **POST /login2** to **Burp Intruder** and change the **verify** parameter to **carlos**, set the payload position at the **mfa-code** to burte-force the verification code
![](../../Img_note/Pasted%20image%2020221207101312.png)

I find out the verification code is 1728
![](../../Img_note/Pasted%20image%2020221207101700.png)

Show the response in browser and complete the lab
![](../../Img_note/Pasted%20image%2020221207102003.png)
