import cv2

# 🏁 Flags: it is the way in which the images must read (-1: unchanged, 0: grayscale, 1: color)
img = cv2.imread("lena.jpg", -1) 
print(img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imread('lena_copy.png', 0)
