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
Second, we determine the movement of the ear. We determine the position of the ear and compare it to its previous position. 



<kbd>
<strong>Addition information:For the position of the ear it is important to check the angle of the camera if the camera is not front facing, it can lead to miss interpretation of the ear position</strong>

</kbd>


---

### Analyzing the Nose

We record nose movements along the left/right (X) and up/down (Y) axes, storing positional data for each frame over 2 seconds. From this data, we calculated the Maximum Range of Motion (The largest displacement of the nose during the 2-second window) and the total Nose Travel Distance (The cumulative Euclidean distance between consecutive nose positions) These metrics were combined to compute the Nose Activity Index, a quantitative measure of nose movement

<kbd>
<strong>Addition information:</strong>

</kbd>


---




