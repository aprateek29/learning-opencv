import cv2

img = cv2.imread('Resources/tom.jpg')
# print(img.shape) # get shape

# imgResize = cv2.resize(img, (284, 450)) # resize
# imgCropped = img[100:, 160:240] # crop image

cv2.imshow('Image', img)
cv2.waitKey(0)