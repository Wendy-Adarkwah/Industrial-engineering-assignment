#import the needed libraries
import cv2
# create a new cam object
cap = cv2.VideoCapture(0)

# initialize the face recognizer (default face haar cascade)
cascade_path = 'C:/Program Files/Python310/Lib/site-packages/cv2/data/haarcascade_frontalcatface.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

while True:
    # read the image from the cam
    _, image = cap.read()

    # detect all the faces in the image
    faces = face_cascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # insert a purple square on each face detected
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 255), thickness=2)
    #name the display window as wendy
    cv2.imshow("wendy", image)
    #quit the operation at the press of key n
    if cv2.waitKey(1) == ord("n"):
        break
#release the camera device from python
cap.release()
cv2.destroyAllWindows()