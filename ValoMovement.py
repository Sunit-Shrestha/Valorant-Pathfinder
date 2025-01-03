from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import pyscreenshot as pss
import keyboard as kb
import time
import cv2
import numpy as np

#All vectors and pixel positions have left to right as +ve X-axis and downwards as +ve Y-axis.

#Returns character position as pixel position in 500x500 map.
def findPosition():
    kb.press_and_release('m')
    map = pss.grab()
    kb.press_and_release('m')
    img = cv2.cvtColor(np.array(map), cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('template.png', 0)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #Converts position from 1280x720 image to 500x500. 
    posX = int((max_loc[0]-411) * 1.106)
    posY = int((max_loc[1]-129) * 1.106)
    return posX, posY

def findDirection():
    forward = 'e'
    initialX, initialY = findPosition()
    kb.press(forward)
    time.sleep(2)
    kb.release(forward)
    finalX, finalY = findPosition()
    dirVec =  [finalX-initialX, finalY-initialY]
    directionCosines = [ dirVec[0] / ( dirVec[0]**2 + dirVec[1]**2 ) ** (1/2), 
    dirVec[1] / ( dirVec[0]**2 + dirVec[1]**2 ) ** (1/2)]
    return directionCosines 

#Moves for maximum of 180 pixels. If path>180, returns False indicating total path hasn't been travelled yet, else it returns True.
def move(dirCos, pathPixels, meterPerPix):
    forward = 'e'; backward = 'd'; left = 's'; right = 'f'
    if len(pathPixels)>50:
        moves = 180
    else:
        moves = len(pathPixels)
    for i in range(moves-1):
        Vector = [ (pathPixels[i+1][0] - pathPixels[i][0]), (pathPixels[i+1][1] - pathPixels[i][1])]
        #Projection formula using character direction cosines. (6.7 is meter per second in-game.)
        straightTime = ( dirCos[0]*Vector[0] + dirCos[1]*Vector[1] ) * meterPerPix / 7
        #Projection formula using direction cosines perpendicular to character.
        sideTime = ( - dirCos[1]*Vector[0] + dirCos[0]*Vector[1] ) * meterPerPix / 7
        if straightTime>=0:
            kb.press(forward)
            time.sleep(straightTime)
            kb.release(forward)
        else:
            kb.press(backward)
            time.sleep(-straightTime)
            kb.release(backward)
        if sideTime>=0:
            kb.press(right)
            time.sleep(sideTime)
            kb.release(right)
        else:
            kb.press(left)
            time.sleep(-sideTime)
            kb.release(left)
    if moves == 180:
        return True
    else:
        return False

def findPath(posX, posY):
    image = cv2.imread('finalMap.png')
    #Image pixel co-ordinates and RGB values are inverted. (y, x) and [B, G, R].
    ascentArray = []
    for x in range(500):
        ascentArray.append([])
        for y in range(500):
            if (image[x,y] == [255,255,255]).all():
                ascentArray[x].append(1)
            else:
                ascentArray[x].append(0)
    grid = Grid(matrix=ascentArray)
    start = grid.node(posX, posY)
    end = grid.node(175, 199)
    finder = AStarFinder()
    path = finder.find_path(start, end, grid)
    for pixel in path[0]:
        image = cv2.circle(image, pixel, radius=0, color = (0, 0, 255), thickness = -1)
    cv2.imwrite('path.png', image)
    return path[0]

def main():
    print("Program Started.")
    directionCosines = findDirection()
    isFinished = False
    while isFinished == False:
        posX, posY = findPosition()
        path = findPath(posX, posY)
        isFinished = move(directionCosines, path, 0.26)

kb.add_hotkey('+', main)
kb.wait()