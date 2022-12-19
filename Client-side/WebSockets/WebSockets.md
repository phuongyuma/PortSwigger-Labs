
### Lab: [Manipulating the WebSocket handshake to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-handshake-to-exploit-vulnerabilities)

	Description: This online shop has a live chat feature implemented using WebSockets. It has an aggressive but flawed XSS filter. To solve the lab, use a WebSocket message to trigger an `alert()` popup in the support agent's browser.


Step 1:  Open the application with browser of **Burp Suite**, check out the features of the applicaton
I come to page **Chat** and make a little chat. But when i input a script, **Live chat** is disconnected.

The web application blocked me.
![](../../Img_note/Pasted%20image%2020221215213525.png)

Step 2: Avoid being blocked
I go to **Proxy > Options** and use  `X-Forwarded-For` to connect to tha web application as a another IP address.
![](../../Img_note/Pasted%20image%2020221215231521.png)

Step 3: Turn on **Burp Intercept** 
Use fuction **Chat** again but turn on **Burp Intercept**. 
![](../../Img_note/Pasted%20image%2020221215232159.png)

![](../../Img_note/Pasted%20image%2020221215231813.png)
![](../../Img_note/Pasted%20image%2020221215232235.png)
