#### Lab: File path traversal, simple case

##### Lab: File path traversal, traversal sequences blocked with absolute path bypass

#### Lab: File path traversal, traversal sequences stripped with superfluous URL-decode

#### Lab: File path traversal, validation of file extension with null byte bypass

First, i go to page of a product and open the image in new tab. Here i can see the file path on the url
> https://0a0b00680395c892c08331fb00de00db.web-security-academy.net/image?filename=5.jpg
![[Pasted image 20221207111235.png]]

I change the **filename** to **filename=etc/passwd**, alternate add "../" before /etc/passwd to go to the parent directory and find where is **etc/passwd**.
Finally, i add **%00.png** after passwd. Add **.png** to avoid validation file extension, **%00** is null bytes.
Reload home page and the lab notify that the lab completed

> /image?filename=/../../../etc/passwd%00.png

[Null bytes injection ](http://projects.webappsec.org/w/page/13246949/Null%20Byte%20Injection)
 ```
Most web applications today are developed using higher-level languages such as, PHP, ASP, Perl, and Java. However, these web applications at some point require processing of high-level code at system level and this process is usually accomplished by using ‘C/C++’ functions. The diverse nature of these dependent technologies has resulted in an attack class called ‘Null Byte Injection’ or ‘Null Byte Poisoning’ attack. In C/C++, a null byte represents the string termination point or delimiter character which means to stop processing the string immediately. Bytes following the delimiter will be ignored. If the string loses its null character, the length of a string becomes unknown until memory pointer happens to meet next zero byte. This unintended ramification can cause unusual behavior and introduce vulnerabilities within the system or application scope. In similar terms, several higher-level languages treat the ‘null byte’ as a placeholder for the string length as it has no special meaning in their context. Due to this difference in interpretation, null bytes can easily be injected to manipulate the application behavior. 
``` 
 

![[Pasted image 20221207102946.png]]
