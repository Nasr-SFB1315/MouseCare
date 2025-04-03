import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import time
from dlclive import Processor
class MouseLickImageProcessor(Processor):
    def __init__(self, green_thresh=3, yellow_thresh=7, weight_earR=1, weight_earL=1, weight_eyeR=1, weight_eyeL=1, weight_nose=1):
        super().__init__()
        #set the threshold for the images
        self.detect_thresh_yellow = yellow_thresh
        self.detect_thresh_green = green_thresh
        #set the weight for the evaluation
        self.weight_earR = weight_earR
        self.weight_earL = weight_earL
        self.weight_eyeR = weight_eyeR
        self.weight_eyeL = weight_eyeL
        self.weight_nose = weight_nose
        #set the values for the eye stress
        self.frame_counter = 0 #for the right eye
        self.eye_state = 0  # 0 = open, 1 = blinking, 2 = squinting
        self.frame_counterL = 0 # now for the left eye
        self.eyeL_state = 0  # 0 = open, 1 = blinking, 2 = squinting
        self.totaleye_stresslevel = 0 # total stress for both eyes combined
         # set the values for the ear stress
        self.earR_frame_counter = 0
        self.earL_frame_counter = 0
        self.earR_fold_state = 0  # 0 = normal, 1 = folded
        self.earL_fold_state = 0  # 0 = normal, 1 = folded
        self.earR_thresh = 20 #this is the proximity to the eye we define as folded. You can adjust it as needed. PS: this is based on pixel values
        self.earL_thresh = 20
        self.earComp_thresh = 20
        self.ear_fold_frames = 20   #this is the number of frames the ear has to be in a position to count
        self.earR_stressLeve = 0    #this is the calculated stress level of the ear
        self.earL_stressLeve = 0
        self.totalear_stresslevel = 0
        self.freeze_value = 10 # this is the value to determine the level of freezing this is done for ears and nose
        self.freeze_frames = 30 # number of frames to determine freezing. Adjust according to framerate
        self.earR_freezstress = 0
        self.earL_freezstress = 0
        self.prev_earR_X = 0
        self.prev_earR_Y = 0
        self.prev_earL_X = 0
        self.prev_earL_Y = 0
        #nose values
        self.Nose_freeze_value = 10
        self.Nose_freeze_frames = 30
        self.prev_Nose_X = 0
        self.prev_Nose_Y = 0
        self.Nose_freezstress = 0
        self.totalnose_stresslevel = 0
        #defining the stressvalue of each facial feature. This can be adjusted as needed
        self.ear_stressFolding = 2.5
        self.ear_stressFreezing = 0.5
        self.eye_stressSqueeze = 1.5
        self.nose_stressFreezing = 1

        #set the rest
        self.feature_accuracy = 0
        self.green_feature_image_path = r"C:\Users\Mein\Desktop\dlcstuff\MouseCare\MG1.png"
        self.red_feature_image_path = r"C:\Users\Mein\Desktop\dlcstuff\MouseCare\MR1.png"
        self.yellow_feature_image_path = r"C:\Users\Mein\Desktop\dlcstuff\MouseCare\MY1.png"
        # Tkinter setup
        self.root = tk.Tk()
        self.root.title("Lick Detection")
        self.image_label = tk.Label(self.root)
        self.image_label.pack()
        self.update_image(initial=True)

    def update_image(self, image_path=None, initial=False):
        """Loads and updates the displayed image"""
        try:
            if initial:
                image_path = self.red_feature_image_path  # Default image
            image = Image.open(image_path)
            image = image.resize((320, 240), Image.Resampling.LANCZOS)
            image = ImageTk.PhotoImage(image)
            self.image_label.config(image=image)
            self.image_label.image = image  # Keep reference
        except Exception as e:
            print(f"Error loading image: {e}")


    def calculate_average_accuracy(self, pose):
        """Calculates the average accuracy of features 0-6"""
        EarR_accuracy_values = pose[0, 2]
        EarL_accuracy_values = pose[1, 2]
        EyeRU_accuracy_values = pose[2, 2]
        EyeRL_accuracy_values = pose[3, 2]
        EyeLU_accuracy_values = pose[4, 2]
        EyeLL_accuracy_values = pose[5, 2]
        Nose_accuracy_values = pose[6, 2]

        total_accuracy_values = [
            EarR_accuracy_values, EarL_accuracy_values, EyeRU_accuracy_values,
            EyeRL_accuracy_values, EyeLU_accuracy_values, EyeLL_accuracy_values, Nose_accuracy_values
        ]

        return np.mean(total_accuracy_values)


    #the function for the  eyes stress detection
    def eye_stress(self, pose):
        #fixed values
        #this is the basic distance we define as eye is closed. In case you change the resolution this might need to be adjuted
        eye_thresh = 5
        #this is the definition of the time it takes to blink in frames if you change the frame rate adjust here
        blink_frames = (5, 20)
        blinkL_frames = (5, 20)
        #this is our definition of how long the eye is squited to be counted as squiting and not blinking rules see the 2 above
        squint_frames = 30

        #evaluating the stress of the right eye

        EyeRU_X, EyeRU_Y = pose[2, 0], pose[2, 1]
        EyeRL_X, EyeRL_Y = pose[3, 0], pose[3, 1]

        # Euclidean distance
        dist = np.sqrt((EyeRU_X - EyeRL_X) ** 2 + (EyeRU_Y - EyeRL_Y) ** 2)

        # Check if eyes are close
        if dist < eye_thresh:
            self.frame_counter += 1
        else:
            self.frame_counter = 0  # Reset if eyes are open

        # Classify the state
        if self.frame_counter == 0:
            self.eye_state = 0  # Eyes open
        elif blink_frames[0] <= self.frame_counter <= blink_frames[1]:
            self.eye_state = 0  # This was to test if blinking is detectable
        elif self.frame_counter >= squint_frames:
            self.eye_state = self.eye_stressSqueeze  # Squinting



        # evaluating the stress level of the left eye



        EyeLU_X, EyeLU_Y = pose[4, 0], pose[4, 1]
        EyeLL_X, EyeLL_Y = pose[5, 0], pose[5, 1]

        # Euclidean distance
        distL = np.sqrt((EyeLU_X - EyeLL_X) ** 2 + (EyeLU_Y - EyeLL_Y) ** 2)

        # Check if eyes are close
        if distL < eye_thresh:
            self.frame_counterL  += 1
        else:
            self.frame_counterL = 0  # Reset if eyes are open

        # Classify the state
        if self.frame_counterL == 0:
            self.eyeL_state = 0  # Eyes open
        elif blinkL_frames[0] <= self.frame_counterL <= blinkL_frames[1]:
            self.eyeL_state = 0  # This was to test if blinking is detectable
        elif self.frame_counterL >= squint_frames:
            self.eyeL_state = self.eye_stressSqueeze  # Squinting

        self.totaleye_stresslevel = (self.eye_state * self.weight_eyeR) + (self.eyeL_state * self.weight_eyeL)


        #The following prints allow for the user to observe the stress via the console in numeric value
        #print("EyeR position stress", self.eye_state)
        #print("EyeL position stress", self.eyeL_state)



        return self.totaleye_stresslevel




    #the function for the right eye stress detection
    def ear_stress(self, pose):




        #loading all the positional data into dfs
        earR_X, earR_Y = pose[0, 0], pose[0, 1]
        EyeRU_X, EyeRU_Y = pose[2, 0], pose[2, 1]
        earL_X, earL_Y = pose[1, 0], pose[1, 1]
        EyeLU_X, EyeLU_Y = pose[4, 0], pose[4, 1]

        #comparing the hight of the right ear to the eye. This is done to determine if the ear is folded

        # Check if right ear is within threshold of eye height. This is done to determine if the ear is folded
        if abs(earR_Y - EyeRU_Y) < self.earR_thresh:
            self.earR_frame_counter += 1
        else:
            self.earR_frame_counter = 0  # Reset if ear is back to normal

        # Classify ear state for right ear
        if self.earR_frame_counter >= self.ear_fold_frames: #this checks the number of frames the ear was folded value can be adjusted
            self.earR_fold_state = 1  # Ear is folded
            self.earR_stressLeve = self.ear_stressFolding
        else:
            self.earR_fold_state = 0  # Ear is normal
            self.earR_stressLeve = 0

        #comparing the hight of the left ear to the eye. This is done to determine if the ear is folded

        if abs(earL_Y - EyeLU_Y) < self.earR_thresh:
            self.earL_frame_counter += 1
        else:
            self.earL_frame_counter = 0  # Reset if ear is back to normal

        # Classify ear state for right ear
        if self.earL_frame_counter >= self.ear_fold_frames: #this checks the number of frames the ear was folded value can be adjusted
            self.earL_fold_state = 1  # Ear is folded
            self.earL_stressLeve = self.ear_stressFolding
        else:
            self.earL_fold_state = 0  # Ear is normal
            self.earL_stressLeve = 0


        #checking the movement of the right ear to check if it is freezing (not the video but the behaviour)

        # Define movement threshold and required duration for freezing
        freeze_value = self.freeze_value  # Movement threshold, everything below counts as freezing
        freeze_frames = self.freeze_frames  # Number of frames freezing needs to occur to count as actual freezing

        # Calculate movement distance
        earR_movement = np.sqrt((earR_X - self.prev_earR_X) ** 2 + (earR_Y - self.prev_earR_Y) ** 2)

        # Check if movement is below threshold
        if earR_movement < freeze_value:
            self.EarR_freeze_frame_counter += 1
        else:
            self.EarR_freeze_frame_counter = 0  # Reset if movement is detected

        # Classify freezing
        if self.EarR_freeze_frame_counter >= freeze_frames:
            freezing_state = 1  # Freezing detected
            self.earR_freezstress = self.ear_stressFreezing

        else:
            freezing_state = 0  # No freezing
            self.earR_freezstress = 0

        # Update previous position
        self.prev_earR_X = earR_X
        self.prev_earR_Y = earR_Y



        #checking the movement of the left ear to check if it is freezing (not the video but the behaviour)

        # Define movement threshold and required duration for freezing
        freeze_value = self.freeze_value  # Movement threshold, everything below counts as freezing
        freeze_frames = self.freeze_frames  # Number of frames freezing needs to occur to count as actual freezing

        # Calculate movement distance
        earL_movement = np.sqrt((earL_X - self.prev_earL_X) ** 2 + (earL_Y - self.prev_earL_Y) ** 2)

        # Check if movement is below threshold
        if earL_movement < freeze_value:
            self.EarL_freeze_frame_counterL += 1
        else:
            self.EarL_freeze_frame_counterL = 0  # Reset if movement is detected

        # Classify freezing
        if self.EarL_freeze_frame_counterL >= freeze_frames:
            freezing_state = 1  # Freezing detected
            self.earL_freezstress = self.ear_stressFreezing

        else:
            freezing_state = 0  # No freezing
            self.earL_freezstress = 0

        # Update previous position
        self.prev_earL_X = earL_X
        self.prev_earL_Y = earL_Y


        #calculate the total stress level caused by both ears and send it back

        self.totalear_stresslevel=(self.earR_stressLeve * self.weight_earR) + (self.earL_stressLeve * self.weight_earL) + (self.earR_freezstress * self.weight_earR) + (self.earL_freezstress * self.weight_earL)


        #The following prints allow for the user to observe the stress via the console in numeric value
        #print("earR position stress", self.earR_stressLeve)
        #print("earL position stress", self.earL_stressLeve)
        #print("earR freeze stress", self.earR_freezstress)
        #print("earL freeze stress", self.earL_freezstress)


        return self.totalear_stresslevel





   #the function for the  eyes stress detection
    def nose_stress(self, pose):
        #fixed values


        #evaluating the stress of the nose

        Nose_X, Nose_Y = pose[6, 0], pose[6, 1]

        #checking the movement of the nose to check if it is freezing (not the video but the behaviour)

        # Define movement threshold and required duration for freezing
        freeze_value = self.Nose_freeze_value  # Movement threshold, everything below counts as freezing
        freeze_frames = self.Nose_freeze_frames  # Number of frames freezing needs to occur to count as actual freezing

        # Calculate movement distance
        Nose_movement = np.sqrt((Nose_X - self.prev_Nose_X) ** 2 + (Nose_Y - self.prev_Nose_Y) ** 2)

        # Check if movement is below threshold
        if Nose_movement < freeze_value:
            self.Nose_freeze_frame_counter += 1
        else:
            self.Nose_freeze_frame_counter = 0  # Reset if movement is detected

        # Classify freezing
        if self.Nose_freeze_frame_counter >= freeze_frames:
             self.Nose_freezstress = self.nose_stressFreezing

        else:
            self.Nose_freezstress = 0

        # Update previous position
        self.prev_Nose_X = Nose_X
        self.prev_Nose_Y = Nose_Y


        self.totalnose_stresslevel=(self.Nose_freezstress * self.weight_nose)


        #The following prints allow for the user to observe the stress via the console in numeric value
        #print("Nose Freeze stress", self.totalnose_stresslevel)


        return self.Nose_freezstress







    def process(self, pose, **kwargs):
        # some important info: the Facial features are based on the video point of view.
        # Second dlc live starts with x=0/y=0 at the top left corner.

        #here is the part where we check which image to show
        eye_state = self.eye_stress(pose)
        ear_stress = self.ear_stress(pose)
        nose_stress = self.nose_stress(pose)

        combined_absolute_stress = eye_state + ear_stress + nose_stress


        #The following prints allow for the user to observe the stress via the console in numeric value
        print("combined eye stress" , eye_state)
        print("combined ear stress" , ear_stress)
        print("combined stress level" , combined_absolute_stress)

        if combined_absolute_stress >= self.detect_thresh_yellow:
            self.update_image(self.red_feature_image_path)
        elif combined_absolute_stress >= self.detect_thresh_green:  #fixed  now excluding values >= 7
            self.update_image(self.yellow_feature_image_path)
        else:  # combined_absolute_stress < 3
            self.update_image(self.green_feature_image_path)
        self.root.update_idletasks()
        self.root.update()
        return pose









    def run_gui(self):
        """Starts the Tkinter main loop."""
        self.root.mainloop()

#note to self
#finished: version 7.81
