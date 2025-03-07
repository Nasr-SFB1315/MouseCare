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

 
### Setting up the camera

To be able to use your camera in dlclive you need to know the correlating index.
In the folder [Camera-Test](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Camera-Test) is a tutorial on how to find it.


<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
First you need to set up camera by clicking on <strong>Init Cam</strong> make sure that it is set to <strong>OpenCVCam</strong> and give it a name. 
Click on <strong>Edit Camera Settings</strong> set the <strong>device</strong> to the corresponding index of the camera you use. You can set the values according to your needs.
</p>

</br>
### Adding MouseCare

To add MouseCare you need go to select the <strong>Processor Dir</strong> and navigate to where you have downloaded [MouseCare](https://github.com/Nasr-SFB1315/MouseCare/tree/main/MouseCare) to



<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
First you need to set up camera by clicking on <strong>Init Cam</strong> make sure that it is set to <strong>OpenCVCam</strong> and give it a name. 
Click on <strong>Edit Camera Settings</strong> set the <strong>device</strong> to the corresponding index of the camera you use. You can set the values according to your needs.
</p>





