# Using the Network
---
We have provided two versions of the network, the [adaptable](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Trained%20Network/adaptable) and the [exported](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Trained%20Network/exported) version.

The exported Version:
Only the exported version can be used with deeplabcut live, but it cannot be further trained or refined.

The adaptable version:
This version can be further trained/refined and, at a later time point, exported. Since it is already trained it is possible that it does not work with your setup in that case we reccomend to create your own network.

### Creating your own network

To create your own network we recommend to use [deeplabcut](https://github.com/DeepLabCut/DeepLabCut). 
When creating your network, the most important part to keep in mind is the ordering of the facial features. The order should be: right ear, left ear, right eye upper eyelid,  right eye lower eyelid,  left eye upper eyelid,  left eye lower eyelid, and nose. This is the order MouseCare expects.  
We recommend starting with 3 5-min videos and 12–20 frames labeled per video. After having the network train for around 50k iterations, it is advisable to test the network on a video and adjust accordingly. 
In addition, we recommend using videos in which the mouse is clearly visible for the entire duration. This helps the network train better.



### TensorFlow vs PyTorch 
While both versions are available with deeplabcut only TensorFlow is available (at the time of writing) with deeplabcut live gui. The goal of MouseCare was to have an easy-to-use solution, and for that, the GUI (graphical user interface) is an important part. Since MouseCare does not require either to function, it can still be used at a later time point with PyTorch.
