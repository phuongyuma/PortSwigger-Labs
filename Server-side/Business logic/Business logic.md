#### Lab 5: Authentication bypass via flawed state machine

	Description: This lab makes flawed assumptions about the sequence of events in the login process. To solve the lab, exploit this flaw to bypass the lab's authentication, access the admin interface, and delete Carlos.

Credential: `wiener:peter`

After login, this web applicaion let we select role : user, content author at page **/role-selector**

Search google and i know to use **target -> site map -> engagement tools -> discovery content** to  find more directory of this web application
I find page **/admin**
![](../../Img_note/Pasted%20image%2020221207150903.png)

We need access to admin interface, so i think i should do something with page **/role-selector**.
First, at request **POST /role-selector**, i try to change the parameter **role** to **admin** but it is impossible.
Second, after login, i try to jump over the **/role-selector** by come directly to **/**, but it is impossible too. So i try again but befory go to **/**, i drop the request **GET /role-selector** by **Burp Intercept**, 

![](../../Img_note/Pasted%20image%2020221207151726.png)

Finally, i come to **Admin panel** and delete accout of **Carlos**
![](../../Img_note/Pasted%20image%2020221207151748.png)


