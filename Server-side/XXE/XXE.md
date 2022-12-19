

### Lab: [Exploiting XInclude to retrieve files](https://portswigger.net/web-security/xxe/lab-xinclude-attack)


	Description: This lab has a "Check stock" feature that embeds the user input inside a server-side XML document that is subsequently parsed. Because you don't control the entire XML document you can't define a DTD to launch a classic XXE attack. To solve the lab, inject an `XInclude` statement to retrieve the contents of the `/etc/passwd` file.


**Step 1**: Open the application with browser of **Burp Suite**, check out the features of the applicaton
When we use function ==Check Stock==, we will sent a request  to server with parameter `ProductID` and `storeID`

According the lab, we need to inject an `XInclude` statement to retrieve the contents of the `/etc/passwd` file.

[XInclude](https://www.w3.org/TR/xinclude/): **xi:include** element can points to an external document

**Step 2**: Script

```
productId=<document xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></document>
```
Note: We can use tag [**foo**](http://www.catb.org/jargon/html/F/foo.html) if you don't know which tag to use
![](../../Img_note/Pasted%20image%2020221212102428.png)

