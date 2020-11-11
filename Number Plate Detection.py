#CAR NUMBER PLATE DETECTION USING WEBCAM
import cv2

imgwidth=640
imgheight=480
#read video
cap=cv2.VideoCapture(0)
cap.set(3,imgwidth)
cap.set(4,imgheight)
cap.set(10,100)
numberplatecascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
minarea=500    
color = (255,0,255)    
count=0
    
#display video
while True:
    success,img=cap.read()
        
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    numberplates = numberplatecascade.detectMultiScale(imggray,1.1,4)
    
    for (x,y,w,h) in numberplates:
        area = w*h
        if area>minarea:
            cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,255),2)
            cv2.putText(img,"Number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color, 2)
            imgROI = img[y:y+h,x:w+x]
            cv2.imshow("numberplate",imgROI)
    
    
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite('/Users/dharmendraverma/Downloads/Python/New projects/Object Detection/Numberplate/NumberPlate_'+str(count)+".jpg", imgROI)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scanned Saved"+str(count),(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
        
    
    
