import numpy as np 
import cv2 

# img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8) # 512x512 image with 3 channels

img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5) # to draw a line (image, start(x,y), end(x,y), color(B,G,R), thickness))
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 0, 255), 5) # arrowed line
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 5) # to draw a rectangle (image, start(x,y), end(x,y), color(B,G,R), thickness))
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1) # to draw a circle (image, center(x,y), radius, color(B,G,R), thickness))
img = cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10, cv2.LINE_AA) # to put text on image (image, text, start(x,y), font, fontScale, color(B,G,R), thickness, lineType)
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1) # to draw an ellipse (image, center(x,y), axes, angle, startAngle, endAngle, color(B,G,R), thickness)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
