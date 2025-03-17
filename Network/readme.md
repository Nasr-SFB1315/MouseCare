 # Using the network

We have created a trained network using the open source software deeplabcut. Awailable to download from the folder trained network.

In case you want to create your own network for tracing facial features we have created the following guide on how to achieve this.


---

### Installation Instructions

<p align="left">
  <span style="display: inline-block; width: 60%;">
     
    <br>  
   This is the installation guide to setup deeplabcut
  </span>
</p>


### Setting up Deep Lab Cut

We recommend using a conda environment:
- [Anaconda ](https://anaconda.org/anaconda)

### Install Dependencies

Dlc gui with gpu:
```bash
code here
```
Dlc  gui without gpu:
```bash
code here
```
activate the environment
```bash
code here
```
install dlc gui
```bash
code here
```
start dlc
```bash
code here
```
---
 
### Exporting a network for DLC live

# Using Python

```bash
import deeplabcut

deeplabcut.export_model(r"full\path\to\config.yaml", iteration=None, shuffle=1, trainingsetindex=0, snapshotindex=None, TFGPUinference=True, overwrite=False, make_tar=True)
e.g.
deeplabcut.export_model(r"full\path\to\target\config.yaml", iteration=None, shuffle=1, trainingsetindex=0, snapshotindex=None, TFGPUinference=True, overwrite=False, make_tar=True)

```


# Using Anaconda

1. Open anaconda as admin (!)

2. Open the environment with Ipython 

```bash
import deeplabcut
deeplabcut.export_model(r"full\path\to\config.yaml", iteration=None, shuffle=1, trainingsetindex=0, snapshotindex=None, TFGPUinference=True, overwrite=False, make_tar=True)

```


