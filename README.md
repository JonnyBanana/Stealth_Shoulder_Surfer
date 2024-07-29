</BR>

![Alt text](https://raw.githubusercontent.com/JonnyBanana/Stealth_Shoulder_Surfer/main/img/asciilog.PNG)

</BR>

<h2>How it Works</h2>

</BR>

The script  takes pictures from a Laptop's Webcam in stealth mode, without opening terminals or images.</BR>
It does not open any terminals and acts completely stealthily (both .pyw and exe files), making it ideal </BR>
for <a href="https://en.wikipedia.org/wiki/Shoulder_surfing_(computer_security)">Shoulder Surfing</a> sessions.
The program saves the pictures captured by the webcam in the user profile folder. </BR>
To avoid overwriting existing images, each new image is saved with an incremental name. The path and name of the</BR>
images can be easily set in the code. I purposely avoided the use of code checks, to avoid the output of error</BR>
prompts, this is to avoid creating suspicion in case the program, for some reason, fails.

</BR>

<b>IMPORTANT NOTE:</b> The .pyw file may need to add the Python binary to PATH in order to be launched correctly.  

</BR>

<b>Guide Here:</b></BR>

https://phoenixnap.com/kb/add-python-to-path

</BR>

Tested on: <b>Win10 Home</b> </BR>
Ver: <b>22H2</b> </BR>
Build: <b>19045.4651</b>

</BR>

<h2>How, and Why, To Use It in a Real Scenario</h2>

</BR>

Nowadays everyone has a smartphone in their pocket, and thus the ability to </BR>
take pictures in very few seconds, so why the need to create a laptop script?</BR>
Well first of all because anyway, in some cases, the gesture of taking a picture via smartphone can create </BR>
suspicion, and then there are some cases where doing things from laptop from a certain concealability.</BR>
Imagine a high-security place, such as an airport, or at a classic coffee shop with free</BR>
wifi conection, where people often bring their laptops with them.</BR>
Wouldn't it be nice to have the ability to do this from a computer, and without arousing any suspicion?

</BR>

As everyone knows usually laptops have the camera on the front (apart from some models with rotating camera, </BR>
such as some models of Acer Spin Series and Lenovo Yoga Series), so when you shoot you need to move out of</BR>
the camera frame, otherwise instead of photographing any data, you will be photographing yourself, at least in</BR>
most of the shots. Any excuse, such as bending down to pick up an alleged object dropped on the ground, will </BR>
more than suffice for the purpose. Keep in mind that the program generally takes 2/5 seconds before taking the</BR>
picture, which gives plenty of time to move.

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

If you want to compile the script yourself, it is possible to do so with the library “pyinstaller”

</BR>

<h5>To install the library:</h5>

</BR> 

```pip install pyinstaller```

</BR>

<h5>Commands to compile the exe:</h5></BR>

Move to the Stealth_Shoulder_Surfer folder</BR> 

```cd path/of/Stealth_Shoulder_Surfer```</BR> 

Then compile the .pyw file with this command:</BR> 

```pyinstaller --onefile --noconsole Stealth_Shoulder_Surfer.pyw```</BR> 

Or if you want to fill in with custom icon:</BR> 

```pyinstaller --onefile --noconsole --icon=icon.ico Stealth_Shoulder_Surfer.pyw```


</BR> 


<h2>Add More Stealth</h2>

</BR> 

The last thing to do to be truly invisible is to turn off the webcam's LED, which lights up every time it clicks. </BR> 
Unfortunately, doing this via software is complex, this is because you have to modify one or more registry keys</BR> 
(not known) that change depending on the brand and model of the webcam. I attempted to write a script that </BR> 
would at least search the registry for suitable keys to make the job easier, but it was impossible for me </BR> 
to terminate such a program. I therefore opted for the “easy way,” but if anyone would like to try their hand at it, </BR> 
some known paths to the drivers and webcam services are:

</BR> 

Key for Device Drivers: </BR> 
Path: <b>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class</b>

</BR> 

Key for Services: </BR> 
Path: <b>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services</b>

</BR> 

Webcam Settings Key:</BR>
Path: <b>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\DeviceAssociation\Devices</b>

</BR>

You can also manually search for keys such as <b>“LED”</b>  , <b>“WEBCAM”</b> or <b>“CAMERA”</b> in the registry search function.

</BR>

In any case, the best solutions are the simplest:


</BR>

* Stickers</BR>
* Paint or Acrylic marker (such as Uni Posca) </BR>
* Disabling the Led at the Hardware level (desoldering, burning, or breaking) </BR>
* A WebCam Cover (opened) </BR>

</BR>

Finally, if you want to change the script icon, without compiling the file, simply create a link</BR>
to the .pyw script and then change the icon from the “properties” option within the link icon menu.

</BR>

Happy Shoulder Surfing to All!

</BR>


<h2>Demo</h2>

</BR>

See on Youtube Here:

</BR>

<a href="https://www.youtube.com/watch?v=pJgi0XaqmqU" target="_blank"><img src="https://raw.githubusercontent.com/JonnyBanana/ASCII_Star_Wars_Opening/main/img/main.PNG" 
alt="BQOD" width="700" height="450" border="100" /></a> 


</BR>

<h2>Stealth Shoulder Surfer #2 (Video Version)</h2>

</BR>

In this version I slightly modified the code to shoot video instead of taking pictures from the webcam. </BR>
The video is saved in .avi format, to get the videos in the best possible quality. By default it is set to shoot </BR>
30-second videos, but it is easily set as needed. It uses the same libs as v1, so no further installation is needed, </BR>
I did not compile an exe because it is more convenient the .pyw file to set the duration of the video (it would </BR>
not have been possible to have the user set the duration, as it requires a gui and would make it less stealthy).
</BR>
Important note, when shooting video the webcam led stays on steady and it is therefore essential to disable </BR>
the led, as explained in the “Add More Stealth” section.

</BR>


<h2>Stealth Shoulder Surfer #3 (Multishot Version)</h2>

</BR>

Finally, I thought a version that takes multiple photos (multishot) would be useful, so I further modified the code. </BR>
In this version, 10 photos are taken with a delay of 1 sec between each shot. To change the settings for the number </BR>
of shots and the delay, simply modify the last function (for i in range(10)). Disabling the led is also essential </BR>
for this version, as the led blinks with every shot, making the session very suspicious....


</BR>

