
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

![App Screenshot](https://i.postimg.cc/7hFs2Pyg/591c5f28-b913-4740-9a51-32165a66b656.jpg)
![App Screenshot](https://i.postimg.cc/J7sRZTLn/c9128718-6063-4f80-b5de-fd5539541cd2.jpg)

## Deployment

To deploy this project run

```bash
  python3 main.py
```


![Logo](https://uasdtu.com/public/l.png)


