import cv2

bnwMap = cv2.imread('mapmaker.png')
res = bnwMap.shape
for x in range(3, res[0]-3):
    for y in range(3, res[1]-3):
        if (bnwMap[x, y] == [0, 0, 0]).all():
            for i in range(x-3, x+4):
                for j in range(y-3, y+4):
                    if (bnwMap[i, j] != [0, 0, 0]).all():
                        bnwMap[i, j] = [100, 100, 100]
cv2.imwrite('finalMap.png', bnwMap)
