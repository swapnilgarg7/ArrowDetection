import cv2 as cv
import numpy as np
import math

def initialize():
    frameWidth = 640
    frameHeight = 480
    
    cap.set(3, frameWidth) #sets width of frame as frameWidth(640)
    cap.set(4, frameHeight) #sets height of frame as frameHeight(480)
    cap.set(10,150) #brightness level

def findAngle(X1,y1,X2,y2):
    
    Y1 = max(y1,y2) #needed for applying formula
    Y2 = min(y1,y2) #needed for applying formula

    angRadians = math.acos((Y1-Y2)/((((X1-X2)**2)+((Y1-Y2)**2))**0.5)) #mathematical formula

    angle = round(math.degrees(angRadians)) #convert angle from radians to degrees

    return angle

def findAngleNew(pt1,pt2,pt3):

    #get x and y positions of the points
    x1,y1 = pt1[0],pt1[1] 
    x2,y2 = pt2[0],pt2[1]
    x3,y3 = pt3[0],pt3[1]

    angRadians = math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2,x1-x2) #mathematical formula
    #atan2 returns value between -pi to pi radians
    
    angle = round(math.degrees(angRadians)) #convert angle from radians to degrees

    if angle<0:
        angle+=360

    return angle

def findDis(pt1,pt2): #mathematical way for finding distance between 2 points
    return((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)**0.5

def detectArrow(img,imgCanny):

    contours, heirarchy = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
    #finds outlines of that mask

    for cnt in contours:
        area = cv.contourArea(cnt) #calculate area of that mask

        if area>1000: #to remove noises/ small objects from getting detected *VALUE CAN BE CHANGED*

            peri = cv.arcLength(cnt, True) #calculate perimeter of outline
            approx = cv.approxPolyDP(cnt, 0.02*peri, True) #gives corners of the mask
            objCor = len(approx) #to store number of corners

            if objCor==7: #arrow has 7 corners

                x, y, w, h = cv.boundingRect(approx) #to find dimensions of shape
                xpos,ypos = (x+(w//2), y+(h//2)) #get positon of centre of shape from dimensions
                
                hsvFrame = cv.cvtColor(img, cv.COLOR_BGR2HSV) #convert image to HSV coloured
                centrePixel = hsvFrame[xpos,ypos] #get centre pixel of the shape as HSV
                hueVal = centrePixel[0] #hue value is H of HSV

                if hueVal<5:

                    #cv.putText(imgContour,"arrow",(xpos,ypos), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,255,255),2) 
                    #temporary, for displaying if arrow got detected or not

                    rect = cv.minAreaRect(cnt) #gets minimum bounded rectangle
                    points = cv.boxPoints(rect) #gets corner points of that rectangle
                    points = np.int0(points) #converts points to integers

                    a = findDis(points[0],points[1]) #find distance between corner1 and corner2
                    b = findDis(points[1],points[2]) #find distance between corner2 and corner3

                    if a>b: #finding longest edge and setting the longest edge's corners as points for angle calculation
                        pt1 = points[0]  
                        pt2 = points[1]

                    else:
                        pt1 = points[1]
                        pt2 = points[2]   

                    angle = findAngle(pt1[0],pt1[1],pt2[0],pt2[1]) #finds angle with vertical axis
                    print("angle is ",angle) #shows the angle

#MAIN CODE STARTS HERE  

cap = cv.VideoCapture(0) #initialise capture from Camera

initialize() 

while True:
    
    ret, img = cap.read() 
    #ret is a boolean value of if the reading of capture worked or not
    #img stores the current frame/image of the camera feed

    imgContour = img.copy()#we will display the arrow detected here instead of in original camera feed

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #converts image to greyscale
    imgBlur = cv.GaussianBlur(imgGray, (7,7), 1) #then blurs the greyscaled image
    imgCanny = cv.Canny(imgBlur,50,50) #finally converts the grey+blurred to Canny image(edges visible)

    detectArrow(img,imgCanny) #current frame/image passed to the detectArrow function

    cv.imshow("Original Camera Feed", img) #shows original camera feed
    cv.imshow('Arrow Detect',imgContour) #shows the image which shows if arrow detected or not

    if cv.waitKey(1) & 0xFF == ord('q'): #let q be the key to be pressed to quit program
        break
