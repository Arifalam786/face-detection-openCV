import cv2

cap = cv2.VideoCapture(1)    # 0 use default web camera
cap.set(3,640)       # width id no 3 as 640
cap.set(4,480)       # height id no 4 as 480
cap.set(10,100)      # brightness id no 10 as 100
def live(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)         #imgGray , scale factor, minimum neighbour

#creating the bounding box
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    return img
while True:
    success, img  = cap.read()
    image = live(img)
    cv2.imshow("Video",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break