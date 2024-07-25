</BR>

![Alt text](https://raw.githubusercontent.com/JonnyBanana/Stealth_Shoulder_Surfer/main/img/asciilog.PNG)

</BR>

<h2>How it Works</h2>

</BR>

The script  takes pictures from a Laptop's Webcam in stealth mode, without opening terminals or images.</BR>
It does not open any terminals and acts completely stealthily (both .pyw and exe files), making it ideal </BR>
for <a href="https://en.wikipedia.org/wiki/Shoulder_surfing_(computer_security)">Shoulder Surfing</a> sessions.
The program saves the pictures captured by the webcam in the user profile folder. </BR>
To avoid overwriting existing images, each new image is saved with an incremental name. </BR>
The path and name of the images can be easily set in the code.</BR>
I purposely avoided the use of code checks, to avoid the output of error prompts, </BR>
this is to avoid creating suspicion in case the program, for some reason, fails.

</BR>

Tested on: <b>Win10 Home</b> </BR>
Ver: <b>22H2</b> </BR>
Build: <b>19045.4651</b>

</BR>

<h2>How, and Why, To Use It in a Real Scenario</h2>

</BR>

Nowadays everyone has a smartphone in their pocket, and thus the ability to </BR>
take pictures in very few seconds, so why the need to create a laptop script?</BR>
Well first of all because anyway, in some cases, the gesture of taking a picture via smartphone can create suspicion, </BR>
and then there are some cases where doing things from laptop from a certain concealability.</BR>
Imagine a high-security place, such as an airport, or at a classic coffee shop </BR>
with free wifi conection, where people often bring their laptops with them.</BR>
Wouldn't it be nice to have the ability to do this from a computer, and without arousing any suspicion?

</BR>

As everyone knows usually laptops have the camera on the front (apart from some models with rotating camera, </BR>
such as some models of Acer Spin Series and Lenovo Yoga Series), so when you shoot you need to move out of the camera frame,</BR>
keep in mind that the program generally takes 2/5 seconds before taking the picture, which gives plenty of time to move.

</BR>

![Alt text](https://raw.githubusercontent.com/JonnyBanana/Stealth_Shoulder_Surfer/main/img/no_data_here.jpg) </br>
<i style="font.size:3px">Example of a photo shot taken with the program (really bad webcam quality)</i>


</BR>


<h2>Requirements</h2>

* Python3
* opencv-python

</BR>  

To install the library:</BR> 


```pip install opencv-python```


</BR> 

Tested on: <b>Python 3.12</b>

</BR> 


<h2>Release</h2>

</BR> 

The exe can be downloaded from here:</BR> 

https://github.com/JonnyBanana/Stealth_Shoulder_Surfer/releases/tag/shoulder_surfing

</BR> 

<h2>How to compile the script</h2>

</BR> 

If you want to compile the script yourself, it is possible to do so with the library “pyinstaller”</BR>

<h5>To install the library:</h5>

</BR> 

```pip install pyinstaller```

</BR>

<h5>Commands to compile the exe:</h5></BR>

Move to the Shadow_Shoulder_Surfer folder</BR> 

```cd path/of/Shadow_Shoulder_Surfer```</BR> 

Then compile the .pyw file with this command</BR> 

```pyinstaller --onefile --noconsole Shadow_Shoulder_Surfer.pyw```


</BR> 

