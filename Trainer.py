from Extraction import Extract
import cv2
import numpy as np

train = Extract()

cap=cv2.VideoCapture(0)
yellow = str(raw_input("Enter the class name for yellow container: "))
green  = str(raw_input("Enter the class name for green container: " ))
red    = str(raw_input("Enter the class name for red container: "   ))
while(True):
	f,img=cap.read()
	x=img.shape[1]
	y=img.shape[0]
	cv2.imshow("Shelf training",img)
	k = cv2.waitKey(60)
	if(k == ord('Q') or ord('q')):
		break
	elif(k == ord('C') or ord('c')):
		cv2.rectangle(img,((int(x*0.2)),int(y*0.00)),((int(x*0.8)),int(y*0.99)),(0,0,255))
	elif(k == ord('S') or ord('s')):
		crop=img[int(y*0.00):int(y*0.99),int(x*0.2):int(x*0.8)]
		train.ext(crop,0)
	elif(k == ord('D') or ord('d')):
                crop=img[int(y*0.00):int(y*0.99),int(x*0.2):int(x*0.8)]
		train.ext(crop,1)
		#take images of not-shelf
	else:
		continue
cv2.destroyAllWindows()

while(True):
	f,img=cap.read()
	x=img.shape[1]
	y=img.shape[0]
	cv2.imshow("Container training",img)
	k=cv2.waitKey(10)
	if(k == ord('Q') or ord('q')):
		break
	elif(k == ord('C') or ord('c')):
		cv2.rectangle(img,((int(x*0.35)),int(y*0.33)),((int(x*0.65)),int(y*0.66)),(255,255,0))
	elif(k == ord('Y') or ord('y')):
                #take images of yellow container
		crop=img[int(y*0.33):int(y*0.66),int(x*0.35):int(x*0.65)]
                train.ext(crop,2)
	elif(k == ord('G') or ord('g')):
                #take images of green container
                crop=img[int(y*0.33):int(y*0.66),int(x*0.35):int(x*0.65)]
		train.ext(crop,3)
	elif(k == ord('R') or ord('r')):
                #take images of red container
                crop=img[int(y*0.33):int(y*0.66),int(x*0.35):int(x*0.65)]
                train.ext(crop,4)
cv2.destroyAllWindows()		
cap.release()
