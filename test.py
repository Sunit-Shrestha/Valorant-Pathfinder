import cv2
import math

image = cv2.imread('finalMap.png')
initPix = [100, 100]
finalPix = [250, 250]
x1 = initPix[0]; y1 = -initPix[1]
x2 = finalPix[0]; y2 = -finalPix[1]
pi = math.pi
pX, pY = [x2-x1, y2-y1]
radius = ( pX**2 + pY**2 ) ** (1/2)
if pX>=0:
    if pX==0 and pY>=0:
        pathAng = 90
    if pX==0 and pY<0:
        pathAng = 270
    if pY>=0:
        pathAng = math.atan(pY/pX)*180/pi
    if pY<0:
        pathAng = 360+math.atan(pY/pX)*180/pi
if pX<0:
    pathAng = 180+math.atan(pY/pX)*180/pi
centre = [x1+radius*math.cos((pathAng-60)*pi/180), y1+radius*math.sin((pathAng-60)*pi/180)]
centrePix = [centre[0], -centre[1]]
print(centre)

