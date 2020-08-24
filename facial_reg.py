import cv2

#image = cv2.imread("BTS.jpg", 1)

#cv2.imshow("People", image)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Now i will be focusing on coding the shape that detects what and where the face of the people are 
f_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

image = cv2.imread("BTS.jpg",1)

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_d = f_cascade.detectMultiScale(grayscale, scaleFactor = 1.05, minNeighbors=5)

for x,y,w,h, in face_d:
    image = cv2.rectangle(image, (x,y), (x+w,y+h), (255,255,255), 2) #(the 255,255,255 is the color that we would like to display
    #then the number after that we have 2 which is there as the size and weight of the shape)

cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()