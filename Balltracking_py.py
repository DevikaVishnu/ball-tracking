# import the necessary packages
import numpy as np
import imutils
import cv2
import time
import serial


#Creating link b/w arduino and python
ser=serial.Serial('/dev/cu.usbmodem1421',9600)
time.sleep(3)

# define the lower and upper boundaries of the "orange"
# ball in the HSV color space, then initialize the
# list of tracked points
orangeLower = (10, 100, 100)
orangeUpper = (38, 191, 253)

#Start camera
camera = cv2.VideoCapture(1)

# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()
    frame=cv2.flip(frame,-1)
    
    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=600)
    #blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # construct a mask for the color "orange", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, orangeLower, orangeUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    
    '''if len(cnts)==0:
        ser.write('b') #Starting readjusting'''
    
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        
        #Stopping readjusting
        
        
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 10 and radius < 134:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), 
            (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            #Moving forward
            ser.write('f')
            print 'Continue Moving', radius
                #if x > 80:
                #ser.write('l')
                #elif x < 75:
                #ser.write('r')
        else:
            ser.write('s') #stop
            print 'x and y and r', x , y , radius




    # show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF


    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        ser.write('s')
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
