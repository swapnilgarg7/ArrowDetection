import cv2 as cv
import numpy as np

def initialize():
    frameWidth = 640
    frameHeight = 480
    
    cap.set(3, frameWidth) #sets width of frame as frameWidth(640)
    cap.set(4, frameHeight) #sets height of frame as frameHeight(480)
    cap.set(10,150) #brightness level

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

                    cv.putText(imgContour,"arrow",(xpos,ypos), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,255,255),2) 
                    #temporary, for displaying if arrow got detected or not

            else:
                break
               



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
