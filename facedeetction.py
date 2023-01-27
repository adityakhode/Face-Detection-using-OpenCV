import cv2
import numpy as np
import time
pre_timeframe = 0
new_timeframe = 0

cap = cv2.VideoCapture(0)# 0  to capture by camera
cap.set(3,1366)# 3 = id no 3 and 640 width
cap.set(4,768)# 4= id no 4 480 is height
cap.set(10,500)# 10= id no 1o for brightness 100


while True: 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
        success,img = cap.read()
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        #imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(img, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (200, 225, 100), 2)
            new_timeframe = time.time()
            z = (new_timeframe-pre_timeframe)
            if z==0:
                z=1
            fps = int(1/z)
            pre_timeframe = new_timeframe
            cv2.putText(img,str(fps),(8,80),cv2.FONT_HERSHEY_SIMPLEX,3,(100,50,60),4)
            # cv2.putText(img,"Aditya",(x),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),0)"""
            cv2.imshow("Adi's Display",img)
cap.release()
cv2.destroyAllWindows()


        