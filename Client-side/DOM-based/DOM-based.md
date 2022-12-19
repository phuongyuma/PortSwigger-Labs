
### Lab: [DOM-based cookie manipulation](https://portswigger.net/web-security/dom-based/cookie-manipulation/lab-dom-cookie-manipulation)

	Description: This lab demonstrates DOM-based client-side cookie manipulation. To solve this lab, inject a cookie that will cause XSS on a different page and call the `print()` function. You will need to use the exploit server to direct the victim to the correct pages.



**Step 1**: Open the application with browser of **Burp Suite**, check out the features of the applicaton

After view a product and back to home, we can see link to **Last View Product**
![](../../Img_note/Pasted%20image%2020221215193427.png)

Come to **HTTP history**, and see request ==GET /== , i find cookie ==LastViewedProduct== and can see changing this attribute to something else is possible.

**Step 2**: Try some changes with the attribute ==LastViewedProduct==
Attempt 1: URL

>LastViewedProduct=https://www.google.com/

![](../../Img_note/Pasted%20image%2020221215194532.png)
I do it in **Burp Repeater** and see the now if we click ==Last View Product==, we will go to google.com

Attempt 2: Script

>LastViewedProduct=abc'?<script>alert(1)</script>

![](../../Img_note/Pasted%20image%2020221215194807.png)
When go to main page, the applicatoin popup an window alert display 1

So i think i will change the url at **LastViewProduct** to `"https://0a42004a04017823c0beb9800028009e.web-security-academy.net/product?productId=1&'><script>print()</script>"`

```
<iframe src="https://0a42004a04017823c0beb9800028009e.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://0a42004a04017823c0beb9800028009e.web-security-academy.net';window.x=1;">
```
Input the above code on exploit server, ==Store== it and ==View Exploit== to check the result
![](../../Img_note/Pasted%20image%2020221215194324.png)

If everything is ok, click ==Delivery to Victim== to finish

![](../../Img_note/Pasted%20image%2020221215200707.png)


