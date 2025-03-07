
# Testing the functionality of your camera
---
Depending on your camera model it might not be supported by deeplabcutlive.
In that case you can use a virtual camera with software like OBS.
- [Open Broadcaster Software | OBS](https://obsproject.com/)





## Find the port for the camera/obs
This python code checks your available camera indexes including virtual cameras

```bash
import cv2

for i in range(10):  # Try indexes 0-9
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera {i} is available")
        cap.release()

```

Here we need to know the index correlating to the camera used example result:
”Camera 0 is available” 
If no camera is available, please check your hardware


### test your video stream
To test your video stream  use the following python code to open a new window showing you the life video feed.

Use the index from given to you by the code above

```bash
import cv2

cap = cv2.VideoCapture(0)  

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Camera Test", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
```
