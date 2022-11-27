import cv2 

# initialize the camera with index 0
cap = cv2.VideoCapture(0) # class for capturing video via webcam (0: default camera, 1: external camera)

# fourcc: 4-byte code used to specify the video codec
# *'XVID': XVID codec 
# 20.0: 20 frames per second
# (640, 480): frame size
out = cv2.VideoWriter('output.mp4', 0x7634706d, 20.0, (640, 480)) # class for saving video (filename, codec, fps, frame size)

print(out.get(cv2.CAP_PROP_FPS)) # get the frame rate of the video
print(cap.isOpened()) # True: if camera is opened, False: if camera is not opened

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 640.0 - width of the frame of the video
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 480.0 - height of the frame of the video
        print(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # -1.0 - number of frames in the video
        out.write(frame) # write the frame to the video
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale (BGR = Blue, Green, Red to GRAY)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):    # 0xFF: 8-bit mask for 64-bit machines (0xFF: 11111111) with q = quit to exit the frame
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()