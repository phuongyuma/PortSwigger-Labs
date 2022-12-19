### Lab: Web shell upload via extension blacklist bypass
[Details](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-extension-blacklist-bypass)

	Description: upload a basic PHP web shell, then use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

Step 1: I open the lab with **Burp Suite** to watch how are files upload to the web application

When i upload an normal image
![](../../Img_note/Pasted%20image%2020221208142233.png)

When i upload a php file
![](../../Img_note/Pasted%20image%2020221208142313.png)

Step 2: Change file .htaccess so that the application accepts a different file extension: ==.hehe==
I fix the filename to .htaccess 
Change content-type to text/plain
Add this Apache directive

> AddType application/x-httpd-php .l33t

![](../../Img_note/Pasted%20image%2020221208150156.png)

Now, we can upload a file **.php** if it chang file extension to **.hehe**

![](../../Img_note/Pasted%20image%2020221208150319.png)

Step 3: Upload malicious file again

![](../../Img_note/Pasted%20image%2020221208152638.png)

Open the image you just upload too see content of **/home/carlos/secret**

![](../../Img_note/Pasted%20image%2020221208152410.png)