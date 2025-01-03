for pixel in path[0]:
    image = cv2.circle(image, pixel, radius=0, color = (0, 0, 255), thickness = -1)
cv2.imwrite('path.png', image