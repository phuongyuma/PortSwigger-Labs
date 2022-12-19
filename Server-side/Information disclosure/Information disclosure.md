#### Lab: Information disclosure in version control history

	Desciption: This lab discloses sensitive information via its version control history. To solve the lab, obtain the password for the `administrator` user then log in and delete Carlos's account.

I use dirsearch to find hidden dir of this application
![](../../Img_note/Pasted%20image%2020221207154557.png)

I found **./git** so i use **wget -r** to install it

After that, i use **git log** to check history of git and found admin password have been removed, so i used **git show 9fc9** to see details of that commit
=> admin password = ba9xn86kkuhz6cjgxdcj
![](../../Img_note/Pasted%20image%2020221207161806.png)

x

Login to admin inteface with **administrator:ba9xn86kkuhz6cjgxdcj**
![](../../Img_note/Pasted%20image%2020221207161939.png)


Delete account of **Carlos** to finish the lab
![](../../Img_note/Pasted%20image%2020221207161959.png)
