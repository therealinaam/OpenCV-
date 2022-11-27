import cv2 

cap = cv2.VideoCapture(0) # 0: default camera, 1: external camera

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):    # 0xFF: 8-bit mask for 64-bit machines (0xFF: 11111111) with q = quit to exit the frame
        break
cap.release()
cv2.destroyAllWindows()