import  cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #for grayscale video stream

    if ret == False:
        continue

    cv2.imshow("Video Frame", frame)
    cv2.imshow("Grayscale Frame", gray_frame)

    #wait for the user input - if q is pressed video will be off
    key_pressed = cv2.waitKey(1) & 0xff
    if key_pressed == ord('q'):
        break

cap.release()   #relese the device
cv2.destroyAllWindows()   #destroy ll windows
