import cv2, time
from datetime import datetime


static_block = None
motions = [None, None]
time = []

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    motion = 0

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayscale = cv2.GaussianBlur(grayscale, (21, 21), 0) 

    if static_block is None:
        static_block = grayscale
        continue

    different_frame = cv2.absdiff(static_block, grayscale)
    thresh_frame = cv2.threshold(different_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    #this section im going to find contours for the moving objects
    cnts,_ = cv2.findContours(thresh_frame.copy(),  
                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts: 
        if cv2.contourArea(contour) < 10000: 
            continue
        motion = 1
  
        (x, y, w, h) = cv2.boundingRect(contour) 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2) 
  
   
    motions.append(motion) 
  
    motions = motions[-2:] 
  
    
    if motions[-1] == 1 and motions[-2] == 0: 
        time.append(datetime.now()) 
    
    if motions[-1] == 0 and motions[-2] == 1: 
        time.append(datetime.now()) 

    cv2.imshow("Gray Frame Captures", grayscale)
    cv2.imshow("Frame captures", different_frame)
    cv2.imshow("Thresh Frame", thresh_frame)
    cv2.imshow("Coloured Frame", frame)

    key = cv2.waitKey()
    if key == ord('z'):
       if motion == 1:
        time.append(datetime.now())
    break
df = pandas.DataFrame(columns = ["Start", "End"]) 

for i in range(0, len(time), 2): 
    df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True)

df.to_csv("Movement Times.csv") 

video.release()
cv2.destroyAllWindows()



