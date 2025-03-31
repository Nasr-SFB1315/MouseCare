 # MouseCare


MouseCare uses the deeplabcut live gui as interface to use the trained network with the stress evaluation software to create a live tracking and evaluation of the face of head fixed mice, to determine their stress

---

### Installation Instructions

<p align="left">
  <span style="display: inline-block; width: 60%;">
    <strong>MouseCare</strong>  
    <br>  
   This is the installation guide to setup deeplabcutlive gui with MouseCare
  </span>
</p>


### Setting up Deep Lab Cut live and MouseCare

We recommend using a conda environment:
- [Anaconda ](https://anaconda.org/anaconda)

### Install Dependencies

Dlc live gui with gpu:
```bash
conda create -n dlc-live python=3.7 tensorflow-gpu==1.13.1
```
Dlc live gui without gpu:
```bash
conda create -n dlc-live python=3.7 tensorflow==1.13.1 
```
activate the environment
```bash
conda activate dlc-live 
```
install dlc live gui
```bash
pip install deeplabcut-live-gui
```
start dlclivegui
```bash
dlclivegui
```


<kbd>
<strong>Addition information:</strong>
Please keep in mind that this guide is for NVIDIA graphic cards. For other graphic cards please follow the instruction of the manufacture
</kbd>


---
 
### Setting up the camera

To be able to use your camera in dlclive you need to know the correlating index.
In the folder [Camera-Test](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Camera-Test) is a tutorial on how to find it.


<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
First you need to set up camera by clicking on <strong>Init Cam</strong> make sure that it is set to <strong>OpenCVCam</strong> and give it a name. 
Click on <strong>Edit Camera Settings</strong> set the <strong>device</strong> to the corresponding index of the camera you use. You can set the values according to your needs. 
</p>
<p align="left">
 <kbd>
<strong>Addition information:</strong>
In regard to resolution and frame rate: Both can be adjusted according to your needs, but if you change frame rate in dlclive you also need to adjust it in MouseCare. We had success with a frame rate of 30fps, which is what we recommend to start with.
Changing the resolution as well as frame rate will change the load on the GPU/CPU. This dependents on the graphics card. For example, a 4090 can handle higher resolution than a 3060. We recommend testing with different resolution and fps to gauge the capability of your setup.
</kbd>
</p>


---

### Adding MouseCare

Make sure you have downloaded [MouseCare](https://github.com/Nasr-SFB1315/MouseCare/tree/main/MouseCare) from the repository.

<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/mousecareImage.png" />
<p align="left">
To add MouseCare you need to go to <strong>Processor Dir</strong>(1) and navigate to the <strong>folder</strong> where you have downloaded MouseCare. 
From the drop-down menu <strong>Processor</strong>(2) and select <strong>MouseCare</strong>. Then press <strong>Edit Proc Settings</strong> to access the settings menu. Here, you can adjust the weights for each facial feature. Once you have made the desired changes, you can finish it by <strong>Update </strong>(3) and initiate it with <strong>Set Proc</strong>(4)
</p>
<kbd>
<strong>Addition information:</strong>
Please make sure that you have MouseCare as well as the init file in the same folder.
</kbd>
</p>


---


### Adding the network

Make sure you have downloaded the [exported network](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Trained%20Network/exported) from the repository. 
<br>



<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/NetworkImage.png" />
<p align="left">
First you add the network via the drop down menu (1). Then you initiate the network (2). You can make adjustments using <strong>Edit DLC Settings</strong> (optional). This tends to take a few seconds. If it takes longer, make sure that you use the GPU and not the CPU.
 
<br>
<br>
At this point you should be able to see the popup of MouseCare with the image repesenting the stress of the mouse.  
For a visual representation of the tracking, you can press <strong>Display DLC Keypoints</strong>(3) to show an overlay of the tracking points. <strong>Edit DLC Display Settings</strong> allows you to adjust the color and size of the overlay dots (optional). 

</p>
<kbd>
<strong>Addition information:</strong>
The network is trained to recognize the facial features of head fixed mice. Given the scope of the project, it is not feasible to train a network to work in every setup imaginable, but it is possible to either train the provided network with new video data from your setup or generate a new network using deeplabcut. Further information are in the folder trained network.

</kbd>
</p>


---

### Setting up the session

At this point, MouseCare should be working and giving feedback on the stress of mice. If you want to have the results as a CSV file, you need to set up a session. 



<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/SessionImage.png" />
<p align="left">
First, you add a name for the subject (1), and a directory (the folder where the data should be stored at) (2). Then you press <strong>Set Up Session</strong>(3). Following this, you can record the session; once you are finished, it is possible to save the video (this will take some time dependent on the length of the recording).



</p>
<kbd>
<strong>Addition information:</strong>
In case you want to use multiple videos or live feeds after another make sure to give them different names to prevent errors
</kbd>
</p>

