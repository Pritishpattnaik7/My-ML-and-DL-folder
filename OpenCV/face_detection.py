import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #for grayscale video stream

    if ret == False:
        continue

    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)  #parameters - 1.3->scale factor 5->no of neighbours


    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("Video Frame", frame)

    #wait for the user input - if q is pressed video will be off
    key_pressed = cv2.waitKey(1) & 0xff
    if key_pressed == ord('q'):
        break

cap.release()   #relese the device
cv2.destroyAllWindows()   #destroy ll windows
