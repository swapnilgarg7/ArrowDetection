
# Arrow Detection

This project detects Red Arrow from a Live Camera Feed and tells the angle the arrow makes with the vertical axis.


## Modules used

[OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

[Numpy](https://numpy.org/)

[Math](https://docs.python.org/3/library/math.html)

## Working of the Program
The program first masks the red colour part of image through HSV values using image segmentation.
Then it detects in the masks the objects that have 7 corners(arrows have 7 corners).
It checks if the area of the object is above 1000pixels as a treshold value to remove small objects.

After this, the minimum rectangle that would bound the arrow is found. 
It's longest edge is taken as the line with which we should calculate the angle of vertical axis with.
The angle is calculated using some maths formulae and displayed.

## Demo Video

[Watch the video by clicking here](https://imgur.com/a/0tBxvL7)

## Deployment

To deploy this project, have python3 installed on your system and then run : 

```bash
pip install opencv-python
```
```bash
python3 main.py
```


