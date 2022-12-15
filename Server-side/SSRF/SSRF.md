
### Lab: [SSRF with blacklist-based input filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter)

	Description: This lab has a stock check feature which fetches data from an internal system. To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`. The developer has deployed two weak anti-SSRF defenses that you will need to bypass   


Step 1: Turn on Burp Suite, open website and check feature of the web with Burp Suite
![](../../Img_note/Pasted%20image%2020221211181438.png)


![](../../Img_note/Pasted%20image%2020221211181339.png)

![](../../Img_note/Pasted%20image%2020221211181409.png)

![](../../Img_note/Pasted%20image%2020221211181234.png)

![](../../Img_note/Pasted%20image%2020221211181215.png)