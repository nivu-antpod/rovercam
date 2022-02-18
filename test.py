import cv2

cap = cv2.VideoCapture ('v4l2src device=/dev/video0 io-mode=2 ! image/jpeg, width=(int)1920, height=(int)1080, framerate=30/1 ! nvv4l2decoder mjpeg=1 ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink', cv2.CAP_GSTREAMER)
                        
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
print("fourcc:{} fps:{}@width:{}@height:{}".format(fourcc, fps, width, height))
file_name = "abc.avi"
out = cv2.VideoWriter(file_name, fourcc, 30, (1920, 1088))
counter = 0
while True:
    if counter > 200:
        break
    counter +=1

    _, frame = cap.read()
    if(frame is None):
        continue


    # cv2.imshow('frame', frame)
    
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    

cap.release()
cv2.destroyAllWindows()