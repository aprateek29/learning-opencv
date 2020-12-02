import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape) # get shape
# img[:] = 255, 0, 0 # color blue
# cv2.line(img, (0,0), (512, 512), (0, 255, 0), 1) # Draw a line
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2) # FILL IT REPLACE 2 WITH CV2.FILLED
# cv2.circle(img, (400, 50), 30, (255, 255, 0), 2) # Draw A Circle

# cv2.putText(img, "OpenCV", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1.4, (0, 150, 0), 1) # put text
cv2.imshow('Image', img)

cv2.waitKey(0)