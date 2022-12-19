### Lab: Web shell upload via extension blacklist bypass
[Details](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-extension-blacklist-bypass)

	Description: upload a basic PHP web shell, then use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

At first i open the lab with **Burp Suite** to watch how are files upload to the web application

When i upload an normal image
![](../../Img_note/Pasted%20image%2020221208142233.png)

When i upload a php file
![](../../Img_note/Pasted%20image%2020221208142313.png)


![](../../Img_note/Pasted%20image%2020221208150156.png)

![](../../Img_note/Pasted%20image%2020221208150319.png)


![](../../Img_note/Pasted%20image%2020221208152638.png)
![](../../Img_note/Pasted%20image%2020221208152410.png)