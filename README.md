
# Arrow Detection

This project was made for UAS-DTU Task 2. It detects Red Arrow from a Live Camera Feed and tells the angle the arrow makes with the vertical axis.


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


## Screenshots

![App Screenshot](https://i.postimg.cc/7hFs2Pyg/591c5f28-b913-4740-9a51-32165a66b656.jpg)
![App Screenshot](https://i.postimg.cc/J7sRZTLn/c9128718-6063-4f80-b5de-fd5539541cd2.jpg)

## Video

[![Watch the video](https://i.postimg.cc/7hFs2Pyg/591c5f28-b913-4740-9a51-32165a66b656.jpg)](https://imgur.com/a/0tBxvL7)

## Deployment

To deploy this project run

```bash
  python3 main.py
```


![Logo](https://uasdtu.com/public/l.png)


