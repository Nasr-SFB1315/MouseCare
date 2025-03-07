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

Make sure you have downloaded [MouseCare](https://github.com/Nasr-SFB1315/MouseCare/tree/main/MouseCare) from the resository.



<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
To add MouseCare you need go to <strong>Processor Dir</strong> and navigate to the <strong>folder</strong> where you have downloaded MouseCare. 
From the drop down menu <strong>Processor</strong> and select <strong>MouseCare</strong>. Then press <strong>Edit Proc Settings</strong> to make sure that everthing is in order. Finish it by <strong>Set Proc</strong>
</p>
<kbd>
<strong>Addition information:</strong>
Please keep in mind once you have added MouseCare to dlclive it will be part of the loading process of dlvlive. This means if you make faulty changes to MouseCare, it will not only crash MouseCare but dlclive as well.
</kbd>
</p>


---



### Adding the network

Make sure you have downloaded the [trained network](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Network) from the resository.



<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
Text here on how to proceed
For firsttime use, we recomment to use our [Accuracy-Test](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Accuracy-Test) first, to see if the network recognises the mouse in the setup accuratly. 
</p>
<kbd>
<strong>Addition information:</strong>
The network is trained to recognise the facial features of head fixed mice. Given the scope of the project it is not possible to train a network to work in every setup imaginable, but it is possible to either train the provided network with new video data from your setup or generate a new network using deeplabcut. The tutorial on how to generate a new netork is here[link]

</kbd>
</p>


---





