import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)) #convert video to grayscale

    if cv2.waitKey (1) & 0xFF == ord('q'): # press q to end video capture
        break

cap.release()
cv2.destroyAllWindows()