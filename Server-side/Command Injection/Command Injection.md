#### Lab 1: Blind OS command injection with output redirection

Description: The application executes a shell command containing in the feedback function when we input, but after executed, the output is not return in the response, so we need use ouput direction. We have provided a writeable folder at **/var/www/images/**

We will insert this to **email** parameter of submit feedback ( i tried insert to **name** parameter but it do not active)

>||whoami>/var/www/images/output.txt||

	Explain: || to split the shell command with input of user


![](../../Img_note/Pasted%20image%2020221207143100.png)

On home page, onpen an image on a new tab, and change **filename=output.txt**. Here, we can see output of command **whoami**
![](../../Img_note/Pasted%20image%2020221207142956.png)


Finally, we go to home page and get the congratulations
![](../../Img_note/Pasted%20image%2020221207143013.png)
