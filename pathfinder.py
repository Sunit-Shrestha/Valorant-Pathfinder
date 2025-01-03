from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import keyboard as kb
import numpy as np
import cv2
import pyscreenshot as pss
import time

image = cv2.imread('finalMap.png')
ascentArray = []
for x in range(500):
    ascentArray.append([])
    for y in range(500):
        if (image[x,y] == [255,255,255]).all():
            ascentArray[x].append(1)
        else:
            ascentArray[x].append(0)
grid = Grid(matrix=ascentArray)
start = grid.node(223, 432)
end = grid.node(175, 199)
finder = AStarFinder()
path = finder.find_path(start, end, grid)
for pixel in path[0]:
    image = cv2.circle(image, pixel, radius=0, color = (0, 0, 255), thickness = -1)
cv2.imwrite('path.png', image)
