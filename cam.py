import cv2
import sys

capture0 = cv2.VideoCapture(0)
capture1 = cv2.VideoCapture(1)
# capture0.set(cv2.CAP_PROP_FPS, 9)
# capture1.set(cv2.CAP_PROP_FPS, 9)


fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

filename0 = "video0.avi"
filename1 = "video1.avi"

if sys.argv[1]:
    filename0 = str(sys.argv[1]) + '0.avi'
    filename1 = str(sys.argv[1]) + '1.avi'

videoWriter = cv2.VideoWriter(filename0, fourcc, 8.0, (640, 480))
videoWriter1 = cv2.VideoWriter(filename1, fourcc, 8.0, (640, 480))

while (True):
 
    ret, frame = capture0.read()
    ret1, frame1 = capture1.read()
     
    if ret:
        cv2.imshow('right', frame)
        cv2.imshow('left', frame1)
        videoWriter.write(frame)
        videoWriter1.write(frame1)
 
    if cv2.waitKey(1) == 27:
        break
 
capture0.release()
capture1.release()
videoWriter.release()
videoWriter1.release()

cv2.destroyAllWindows()
