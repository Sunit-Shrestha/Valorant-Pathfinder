import cv2
import time

map = cv2.imread('Ascent_minimap500.png')
res = map.shape
for x in range(res[0]):
    for y in range(res[1]):
        if (map[x, y] == [126, 127, 126]).all() or (map[x, y] == [137, 163, 165]).all():
            map[x, y] = [255, 255, 255]
        else:
            map[x, y] = [0, 0, 0]

cv2.imwrite('mapmaker.png', map)

