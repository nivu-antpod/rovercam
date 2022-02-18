import cv2
width=640
height=480

cam=cv2.VideoCapture('/dev/video1')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width )
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height )

outVid=cv2.VideoWriter('myCam.avi', cv2.VideoWriter_fourcc(*'XVID'),25,(width, height))
while True:
    ret, frame= cam.read()
    cv2.imshow('nanoCam', frame)
    outVid.write(frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
outVid.release()
cv2.destroyAllWindows()
