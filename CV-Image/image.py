import cv2

# 🏁 Flags: it is the way in which the images must read (-1: unchanged, 0: grayscale, 1: color)
img = cv2.imread("lena.jpg", -1) 
print(img)
cv2.imshow('Image', img)
k = cv2.waitKey(0)  # Wait for a key to be pressed
if k == 27:         # 27: Value of **Escape key** on keyboard 
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
