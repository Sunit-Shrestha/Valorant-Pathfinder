import time
import keyboard as kb
import cv2
import pyscreenshot as pss
import numpy as np

time.sleep(5)
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
print([posX, posY])