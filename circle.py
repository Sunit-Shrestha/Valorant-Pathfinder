import cv2
import math
import random

#Finds slope angle of vector. [0, 360].
def findAngle(x, y):
    if x>=0:
        if x==0 and y>=0:
            angle = pi/2
        if x==0 and y<0:
            angle = 3*pi/2
        if y>=0:
            angle = math.atan(y/x)
        if y<0:
            angle = 2*pi+math.atan(y/x)
    if x<0:
        angle = pi+math.atan(y/x)
    return angle

image = cv2.imread('finalMap.png')
initPix = [100, 100]
finalPix = [250, 250]
x1 = initPix[0]; y1 = -initPix[1]
x2 = finalPix[0]; y2 = -finalPix[1]
pi = math.pi
#Path vector coordinates.
pX, pY = [x2-x1, y2-y1]
radius = ( pX**2 + pY**2 ) ** (1/2)
pathAng = findAngle(pX, pY)
h, k = [x1+radius*math.cos(pathAng-pi/3), y1+radius*math.sin(pathAng-pi/3)]
centrePix = [h, -k]
cirVecX1, cirVecY1 = [x1-h, y1-k]
cirVecAngX = findAngle(cirVecX1, cirVecY1)*180/pi
cirVecX1, cirVecY1 = [x2-h, y2-k]
cirVecAngY = findAngle(cirVecX1, cirVecY1)*180/pi
while x1!=x2 and y1!=y2:
    x1 = int(h+radius*math.cos(cirVecAngX*pi/180))
    y1 = int(k+radius*math.sin(cirVecAngX*pi/180))
    image = cv2.circle(image, [x1, -y1], radius=1, color = (0, 0, 255), thickness = -1)
    cirVecAngX -= 1
cv2.imwrite('path.png', image)




