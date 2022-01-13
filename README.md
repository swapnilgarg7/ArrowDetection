
# Arrow Detection

This project was made for UAS-DTU Task 2. It detects Red Arrow from a Live Camera Feed and tells the angle the arrow makes with the vertical axis.


## Modules used

[OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

[Numpy](https://numpy.org/)

## Working of the Program
The program first tries to detect the red objects
within the camera frame (Ignoring small red ones)
and creates its mask using Image Segmentation.
Next, it checks whether the red object detected has 7 corners or not.
If it does, then it is detected as a Red Arrow.



## Screenshots

![App Screenshot](https://ibb.co/vQrvYTy)
![App Screenshot](https://ibb.co/JjKLh6x)

## Deployment

To deploy this project run

```bash
  python3 main.py
```


![Logo](https://uasdtu.com/public/l.png)


