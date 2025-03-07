# MouseCare


GUI to run DeepLabCut-live on a video feed with the MouseCare stress evaluation software

---

## Installation Instructions

<p align="left">
  <span style="display: inline-block; width: 60%;">
    <strong>MouseCare</strong>  
    <br>  
   MouseCare uses the deeplabcut live gui as interface to use the trained network with the stress evaluation software to create a live tracking and evaluation of the face of head fixed mice, to determine their stress.
  </span>
</p>


### Setting up Deep Lab Cut live and MouseCare

We recommend using a conda environment:
- [Deep Lab Cut live installation guide](https://github.com/DeepLabCut/DeepLabCut-live-GUI?tab=readme-ov-file)

#### Install Dependencies

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




 
##### Next steps

We recommend to use the version XXX
