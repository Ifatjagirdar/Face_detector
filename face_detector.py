import cv2 

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect faces in
#image = cv2.imread('ROJ.png')
webcam = cv2.VideoCapture(r'C:\Users\jagir\OneDrive\Desktop\ifat.mp4')

while True:
    successful_frame_read, frame = webcam.read()

    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_image)
    
    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,256,0),10)
    
    
    cv2.imshow('Face Detector',frame)
    
    key = cv2.waitKey(1)
    
    if key==81 or key==113:
        break
    
    
    
        




