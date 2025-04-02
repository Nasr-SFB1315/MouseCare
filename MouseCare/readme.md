 # MouseCare


MouseCare is a python based solution to evaluate the stress of mice based on tracked facial features. The software is available to download from this folder. 
Following are the basic concepts on which the stress evaluation is based on. 
This description is seperated into the different facial features and how they are evaluated to better understand the code.

---

### Obtaining the positional data of the facial features:

By integrating MouseCare into dlc live we can get the positional data (x and y coordinates) of each facial feature, stored in a data frame ordered by frame it was collected. 
It is important to update the <strong>FrameRate</strong> variable in the code to be the same as the video. 

### Analyzing the eyes

We measure the distance of the upper and lower eye lids using the euclidean distance (d = √[(x2 – x1)2 + (y2 – y1)2]) averaging the x and y over the fps.

<kbd>
<strong>Addition information: The dataframe is analyzed to count consecutive entries where the eyelids remain close together, this is done to exclude rapid blinking</strong>

</kbd>

---
 
### Analyzing the Ear

We use two different metrics to determine the stress based on the ears. <br>
First, we determine their relative position to the eyes. When the Y value of the ear is closer in value to the Y value of the eye, it means that the ear is folded back.   <br>
Second, we determine the movement of the ear. We determine the position of the ear and compare it to its previous position to determine freezing.



<kbd>
<strong>Addition information:For the position of the ear it is important to check the angle of the camera if the camera is not front facing, it can lead to miss interpretation of the ear position</strong>

</kbd>


---

### Analyzing the Nose

We record nose movements along the left/right (X) and up/down (Y) axes, storing positional data for each frame. From this data, we calculated the range of motion (The Euclidean distance between nose positions). These metrics were combined to determine nose freezing. 




---

### Advanced information
To give maximum flexibility, we have added multiple ways to adjust MouseCare to your needs. Following are the explanations on those adjustmend and what they affect.
<br>
<br>
adjustable via the gui:
<br>
        green_thresh: this value determines the stress value on a scale from 1-10 until it switches from green to yellow<br>
        yellow_thresh: this value determines the stress value on a scale from 1-10 until it switches from yellow to red<br>
<br>
Weights:
<br>
        weight_earR: this is the weight of the right ear to modify the impact of the facial feature on the stress evaluation<br>
        weight_earL: this is the weight of the left ear to modify the impact of the facial feature on the stress evaluation<br>
        weight_eyeR: this is the weight of the right eye to modify the impact of the facial feature on the stress evaluation<br>
        weight_eyeL: this is the weight of the left eye to modify the impact of the facial feature on the stress evaluation<br>
        weight_nose: this is the weight of the nose to modify the impact of the facial feature on the stress evaluation<br>

<br>
facial feauture threshold:
<br>
     Ear:
        To determine the folding of the ear we compare the position of the ear with the eye. To do so we have a set a threshold. The smaler the number more the ear needs to be folded to count as folded<br><br>
          self.earR_thresh<br>
          self.earL_thresh<br><br>
          We also determine how long the ear is folded. This is done to exclude false flags due to ear movment.<br><br>        
             self.ear_fold_frames = 20   #this is the number of frames the ear has to be in a position to count<br><br>
        In addition we measure the general movement of the ear to determine the stress level of the ear due to freezing.<br>
        This is done by comparing previous positions with the current position to determine the distance traveld.<br><br>     
             self.freeze_value = 10  <br>
             This is the range of motion we determine counts as freezing. <br>
             The bigger the number the more generous is the system to classify something as freezing.<br><br>             
             self.freeze_frames = 30  <br>
             This is the number of frames to determine freezing. Adjust according to framerate<br><br>
     Nose:<br>
        To determine freezing of the nose we have we measured the general movement of the nose.<br>
        This is done by comparing previous positions with the current position to determine the distance traveld.<br><br>
            self.Nose_freeze_value = 10  this is the range of motion we determine counts as freezing. The bigger the number the more generous is the system to classify something as freezing.<br>
            self.Nose_freeze_frames = 30  number of frames to determine freezing. Adjust according to framerate<br><br>
     Defining the stress value of each facial feature:  <br>
        We have set a value for each type of facial feature to determine the stress it can cause. This is a more complex way of changing the stress value compared to the weights.<br><br>        
        self.ear_stressFolding = 2.5<br>
        self.ear_stressFreezing = 0.5<br>
        self.eye_stressSqueeze = 1.5<br>
        self.nose_stressFreezing = 1<br>
<br>


