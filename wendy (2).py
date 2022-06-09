#we import the libraries of the packages we need
import cv2
import numpy

#we import an image from the computer and use the location of the image
original = cv2.imread(r'this.jpg')
#we make a copy of the original image imported
new= original.copy()

#we show the original image
cv2.imshow('Wendy', original)
while True:
    #image closes when we press x
    if cv2.waitKey(1) == ord("x"):
        break
        #we set the scale values for alpha and beta to use for brightning
alpha = 1.5
beta = 0
#we apply the set values to the image
now = cv2.convertScaleAbs(new, alpha=alpha, beta=beta)
#show the new image
cv2.imshow('brighter',now)
while True:
    #cut the displaying of the new image
    if cv2.waitKey(2) == ord("x"):
        cv2.destroyAllWindows()
        break
