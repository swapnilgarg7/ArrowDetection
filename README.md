
# Arrow Detection

This project was made for UAS-DTU Task 2. It detects Red Arrow from a Live Camera Feed and tells the angle the arrow makes with the vertical axis.


## Modules used

[OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

[Numpy](https://numpy.org/)

[Math](https://docs.python.org/3/library/math.html)

## Working of the Program
The program first converts the live camera feed image into
a Canny image and then detect objects with 7 corners
within the camera frame(Ignoring small ones).
Then it converts the image into HSV format so that
it can then detect which of those 7 cornered objects were red in colour.
If it does, it is detected as a Red Arrow. 

After this, the minimum rectangle that would bound the arrow is found. 
It's longest edge is taken as the line with which we should calculate the angle of vertical axis with.
The angle is calculated using some maths formulae and displayed.


## Screenshots

![App Screenshot](https://i.postimg.cc/7hFs2Pyg/591c5f28-b913-4740-9a51-32165a66b656.jpg)
![App Screenshot](https://i.postimg.cc/J7sRZTLn/c9128718-6063-4f80-b5de-fd5539541cd2.jpg)

## Deployment

To deploy this project run

```bash
  python3 main.py
```


![Logo](https://uasdtu.com/public/l.png)


