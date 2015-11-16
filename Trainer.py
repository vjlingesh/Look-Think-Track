from Extraction import Extract
import cv2
import numpy as np

train = Extract()
cap=cv2.VideoCapture(1)
i=0



while(True): #Grid
        f,img=cap.read()
        x=img.shape[1]
        y=img.shape[0]
        cv2.rectangle(img,((int(x*0.2)),int(y*0.00)),((int(x*0.8)),int(y*0.99)),(0,0,255))
        cv2.imshow("Shelf training",img)
        if(cv2.waitKey(50) & 0xFF == ord('n')):
		break
i=0

while(True): #Shelf training
	f,img=cap.read()
        x=img.shape[1]
        y=img.shape[0]
        cv2.rectangle(img,((int(x*0.2)),int(y*0.00)),((int(x*0.8)),int(y*0.99)),(0,0,255))
        cv2.imshow("Shelf training",img)
	crop=img[int(y*0.00):int(y*0.99),int(x*0.2):int(x*0.8)]
        train.ext(crop,0)
	i=i+1
	print i
	if(cv2.waitKey(50) & 0xFF == ord('n')):
		break
i=0
while(True): #Interval
	f,img=cap.read()
        cv2.imshow("Shelf training",img)
	if(cv2.waitKey(50) & 0xFF == ord('n')):
		break
i=0
while(True): #Non shelf training
	f,img=cap.read()
        cv2.imshow("Shelf training",img)
        train.ext(img,1)
	i=i+1
	print i
	if(cv2.waitKey(50) & 0xFF == ord('n')):
		break
i=0
while(True): #Grid
        f,img=cap.read()
        x=img.shape[1]
        y=img.shape[0]
        cv2.rectangle(img,((int(x*0.35)),int(y*0.33)),((int(x*0.65)),int(y*0.66)),(255,255,0))
        cv2.imshow("Shelf training",img)
        if(cv2.waitKey(50) & 0xFF == ord('n')):
		break

i=0
while(True): #Container 1 Training
	f,img=cap.read()
        x=img.shape[1]
        y=img.shape[0]
        cv2.rectangle(img,((int(x*0.35)),int(y*0.33)),((int(x*0.65)),int(y*0.66)),(255,255,0))
        cv2.imshow("Shelf training",img)
	crop=img[int(y*0.33):int(y*0.66),int(x*0.35):int(x*0.65)]
        train.ext(crop,2)
	i=i+1
	print i
	if(cv2.waitKey(50) & 0xFF == ord('n')):
		break
i=0
while(True): #Interval
	f,img=cap.read()
	cv2.rectangle(img,((int(x*0.35)),int(y*0.33)),((int(x*0.65)),int(y*0.66)),(255,255,0))
        cv2.imshow("Shelf training",img)
	if(cv2.waitKey(50) & 0xFF == ord('n')):
		break
i=0
while(True): #Container 2 Training
	f,img=cap.read()
        x=img.shape[1]
        y=img.shape[0]
        cv2.rectangle(img,((int(x*0.35)),int(y*0.33)),((int(x*0.65)),int(y*0.66)),(255,255,0))
        cv2.imshow("Shelf training",img)
	crop=img[int(y*0.33):int(y*0.66),int(x*0.35):int(x*0.65)]
        train.ext(crop,3)
	i=i+1
	print i
	if(cv2.waitKey(50) & 0xFF == ord('n')):
		break
i=0
while(True): #Interval
	f,img=cap.read()
	cv2.rectangle(img,((int(x*0.35)),int(y*0.33)),((int(x*0.65)),int(y*0.66)),(255,255,0))
        cv2.imshow("Shelf training",img)
	if(cv2.waitKey(50) & 0xFF == ord('n')):
		break

while(True): #Container 3 Training
	f,img=cap.read()
        x=img.shape[1]
        y=img.shape[0]
        cv2.rectangle(img,((int(x*0.35)),int(y*0.33)),((int(x*0.65)),int(y*0.66)),(255,255,0))
        cv2.imshow("Shelf training",img)
	crop=img[int(y*0.33):int(y*0.66),int(x*0.35):int(x*0.65)]
        train.ext(crop,4)
	i=i+1
	print i
	if(cv2.waitKey(50) & 0xFF == ord('n')):
		break

cv2.destroyAllWindows()
cap.release()
