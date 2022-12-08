#### Lab 13 : Referer-based access control

	Description: This lab controls access to certain admin functionality based on the Referer header. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`. Log in using the credentials `wiener:peter` and exploit the flawed to promote yourself to become an administrator.

Note: **Refered header** tell where url starts
First, i login with **administrator** account and observe it on Burp Suite
Go to Admin panel and we have **/admin** can upgrade user to administrator.
The lab request we login with a credential not have admin's premission and exploit the flawde to promote this credential to become an admin.
As the description of this lab, i think i need to do some thing with Referer header of this application

Attempt 1: 
I login with **wiener**'s account and try to jump to page **/admin**, this is not Okay
![](../../Img_note/Pasted%20image%2020221208110301.png)

Attempt 2:
When i upgrade **Carlos**'s account, i see this request has been sent,  attention at **Refered** is **/admin**
![](../../Img_note/Pasted%20image%2020221208105746.png)
I sent this request to **Burp Repeater**, change username=wiener, but this is invalid
![](../../Img_note/Pasted%20image%2020221208114139.png)

Attempt 3:
I login with **wiener:peter**, sent request **GET /my-account**, change url to **/admin-roles?username=wiener&action=upgrade** and fix **Refered** to **/admin**

![](../../Img_note/Pasted%20image%2020221208120125.png)
Finally, i reload the page and see **wiener**'s accout have admin panel
![](../../Img_note/Pasted%20image%2020221208120329.png)