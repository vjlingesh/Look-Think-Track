from Bay import Brain
from Bay_RGB import Brain2
from Track import Eye
import cv2
import numpy as np
import time

think = Brain()
see = Eye()
think2 = Brain2()

boxA = [[0 for i in range(2)] for j in range(2)]
boxB = [[0 for i in range(2)] for j in range(2)]
boxC = [[0 for i in range(2)] for j in range(2)]
boxD = [[0 for i in range(2)] for j in range(2)]
box1 = [[0 for i in range(2)] for j in range(2)]
box2 = [[0 for i in range(2)] for j in range(2)]
box3 = [[0 for i in range(2)] for j in range(2)]
box4 = [[0 for i in range(2)] for j in range(2)]
box5 = [[0 for i in range(2)] for j in range(2)]
box6 = [[0 for i in range(2)] for j in range(2)]
cropimg = [0 for i in range(6)]
index = [[0 for i in range(2)] for j in range(6)]
font = cv2.FONT_HERSHEY_SIMPLEX
cap=cv2.VideoCapture(0)

while(True):
	f,img=cap.read()
	x=img.shape[1]
	y=img.shape[0]
	#A 
	boxA[0][0]=int(x*0.8-x*0.3*0.125) 	#x1
	boxA[0][1]=int(y*0.99-y*0.3*0.125)	#y1
	boxA[1][0]=int(x*0.8)               	#x2  
	boxA[1][1]=int(y*0.99)			#y2

	#B
	boxB[0][0]=int(x*0.2) 			#x1
	boxB[0][1]=int(y*0.99-y*0.3*0.125)	#y1
	boxB[1][0]=int(x*0.2+x*0.3*0.125)   	#x2
	boxB[1][1]=int(y*0.99)			#y2

	#C
	boxC[0][0]=int(x*0.8-x*0.3*0.125) 	#x1
	boxC[0][1]=int(y*0.00)			#y1
	boxC[1][0]=int(x*0.8)               	#x2 
	boxC[1][1]=int(y*0.33*0.125)		#y2

	#D
	boxD[0][0]=int(x*0.2)			#x1
	boxD[0][1]=int(y*0.00)			#y1
	boxD[1][0]=int(x*0.2+x*0.3*0.125)	#x2 
	boxD[1][1]=int(y*0.33*0.125)		#y2

	#UL
	box1[0][0]=int(x*0.2)			#x1
	box1[0][1]=int(y*0.00)			#y1
	box1[1][0]=int(x*0.5)			#x2 
	box1[1][1]=int(y*0.33)			#y2
	#UR
	box2[0][0]=int(x*0.5)			#x1
	box2[0][1]=int(y*0.00)			#y1
	box2[1][0]=int(x*0.8)			#x2 
	box2[1][1]=int(y*0.33)			#y2
	#ML
	box3[0][0]=int(x*0.2)			#x1
	box3[0][1]=int(y*0.33)			#y1
	box3[1][0]=int(x*0.5)			#x2 
	box3[1][1]=int(y*0.66)			#y2
	#MR
	box4[0][0]=int(x*0.5)			#x1
	box4[0][1]=int(y*0.33)			#y1
	box4[1][0]=int(x*0.8)			#x2 
	box4[1][1]=int(y*0.66)			#y2
	#LL
	box5[0][0]=int(x*0.2)			#x1
	box5[0][1]=int(y*0.66)			#y1
	box5[1][0]=int(x*0.8)			#x2 
	box5[1][1]=int(y*0.99)			#y2
	#LR
	box6[0][0]=int(x*0.5)			#x1
	box6[0][1]=int(y*0.66)			#y1
	box6[1][0]=int(x*0.8)			#x2 
	box6[1][1]=int(y*0.99)			#y2

	cv2.rectangle(img,(box1[0][0],box1[0][1]),(box1[1][0],box1[1][1]),(0,0,255))			#UL
	cv2.rectangle(img,(box2[0][0],box2[0][1]),(box2[1][0],box2[1][1]),(0,0,255))			#UR
	cv2.rectangle(img,(box3[0][0],box3[0][1]),(box3[1][0],box3[1][1]),(0,0,255))			#ML
	cv2.rectangle(img,(box4[0][0],box4[0][1]),(box4[1][0],box4[1][1]),(0,0,255))			#MR
	cv2.rectangle(img,(box5[0][0],box5[0][1]),(box5[1][0],box5[1][1]),(0,0,255))			#LL
	cv2.rectangle(img,(box6[0][0],box6[0][1]),(box6[1][0],box6[1][1]),(0,0,255))			#LR
	
	cv2.rectangle(img,(boxD[0][0],boxD[0][1]),(boxD[1][0],boxD[1][1]),(0,0,255))			#D
	cv2.rectangle(img,(boxC[0][0],boxC[0][1]),(boxC[1][0],boxC[1][1]),(0,0,255))			#C
	cv2.rectangle(img,(boxB[0][0],boxB[0][1]),(boxB[1][0],boxB[1][1]),(0,0,255))			#B
	cv2.rectangle(img,(boxA[0][0],boxA[0][1]),(boxA[1][0],boxA[1][1]),(0,0,255))			#A

	A = img[box1[0][1]:box1[1][1], box1[0][0]:box1[1][0]]
	B = img[box2[0][1]:box2[1][1], box2[0][0]:box2[1][0]]
	C = img[box3[0][1]:box3[1][1], box3[0][0]:box3[1][0]]
	D = img[box4[0][1]:box4[1][1], box4[0][0]:box4[1][0]]
	E = img[box5[0][1]:box5[1][1], box5[0][0]:box5[1][0]]
	F = img[box6[0][1]:box6[1][1], box6[0][0]:box6[1][0]]

	resA = think.detect(A)
	resB = think.detect(B)
	resC = think.detect(C)
	resD = think.detect(D)
	resE = think.detect(E)
	resF = think.detect(F)

	if (resA == 0.0):
		cv2.putText(img,'Shelf',(box1[0][0],box1[0][1]+100), font, 1,(255,255,255),2)
	elif (resA == 1.0):
		cv2.putText(img,'Unknown',(box1[0][0],box1[0][1]+100), font, 1,(255,255,255),2)
	elif (resA == 2.0):
		cv2.putText(img,'Container 1',(box1[0][0],box1[0][1]+100), font, 1,(255,255,255),2)
	elif (resA == 3.0):
		cv2.putText(img,'Container 2',(box1[0][0],box1[0][1]+100), font, 1,(255,255,255),2)
	elif (resA == 4.0):
		cv2.putText(img,'Container 3',(box1[0][0],box1[0][1]+100), font, 1,(255,255,255),2)
	if (resB == 0.0):
		cv2.putText(img,'Shelf',(box2[0][0],box2[0][1]+100), font, 1,(255,255,255),2)
	elif (resB == 1.0):
		cv2.putText(img,'Unknown',(box2[0][0],box2[0][1]+100), font, 1,(255,255,255),2)
	elif (resB == 2.0):
		cv2.putText(img,'Container 1',(box2[0][0],box2[0][1]+100), font, 1,(255,255,255),2)
	elif (resB == 3.0):
		cv2.putText(img,'Container 2',(box2[0][0],box2[0][1]+100), font, 1,(255,255,255),2)
	elif (resB == 4.0):
		cv2.putText(img,'Container 3',(box2[0][0],box2[0][1]+100), font, 1,(255,255,255),2)
	if (resC == 0.0):
		cv2.putText(img,'Shelf',(box3[0][0],box3[0][1]+100), font, 1,(255,255,255),2)
	elif (resC == 1.0):
		cv2.putText(img,'Unknown',(box3[0][0],box3[0][1]+100), font, 1,(255,255,255),2)
	elif (resC == 2.0):
		cv2.putText(img,'Container 1',(box3[0][0],box3[0][1]+100), font, 1,(255,255,255),2)
	elif (resC == 3.0):
		cv2.putText(img,'Container 2',(box3[0][0],box3[0][1]+100), font, 1,(255,255,255),2)
	elif (resC == 4.0):
		cv2.putText(img,'Container 3',(box3[0][0],box3[0][1]+100), font, 1,(255,255,255),2)
	if (resD == 0.0):
		cv2.putText(img,'Shelf',(box4[0][0],box4[0][1]+100), font, 1,(255,255,255),2)
	elif (resD == 1.0):
		cv2.putText(img,'Unknown',(box4[0][0],box4[0][1]+100), font, 1,(255,255,255),2)
	elif (resD == 2.0):
		cv2.putText(img,'Container 1',(box4[0][0],box4[0][1]+100), font, 1,(255,255,255),2)
	elif (resD == 3.0):
		cv2.putText(img,'Container 2',(box4[0][0],box4[0][1]+100), font, 1,(255,255,255),2)
	elif (resD == 4.0):
		cv2.putText(img,'Container 3',(box4[0][0],box4[0][1]+100), font, 1,(255,255,255),2)
	if (resE == 0.0):
		cv2.putText(img,'Shelf',(box5[0][0],box5[0][1]+100), font, 1,(255,255,255),2)
	elif (resE == 1.0):
		cv2.putText(img,'Unknown',(box5[0][0],box5[0][1]+100), font, 1,(255,255,255),2)
	elif (resE == 2.0):
		cv2.putText(img,'Container 1',(box5[0][0],box5[0][1]+100), font, 1,(255,255,255),2)
	elif (resE == 3.0):
		cv2.putText(img,'Container 2',(box5[0][0],box5[0][1]+100), font, 1,(255,255,255),2)
	elif (resE == 4.0):
		cv2.putText(img,'Container 3',(box5[0][0],box5[0][1]+100), font, 1,(255,255,255),2)
	if (resF == 0.0):
		cv2.putText(img,'Shelf',(box6[0][0],box6[0][1]+100), font, 1,(255,255,255),2)
	elif (resF == 1.0):
		cv2.putText(img,'Unknown',(box6[0][0],box6[0][1]+100), font, 1,(255,255,255),2)
	elif (resF == 2.0):
		cv2.putText(img,'Container 1',(box6[0][0],box6[0][1]+100), font, 1,(255,255,255),2)
	elif (resF == 3.0):
		cv2.putText(img,'Container 2',(box6[0][0],box6[0][1]+100), font, 1,(255,255,255),2)
	elif (resF == 4.0):
		cv2.putText(img,'Container 3',(box6[0][0],box6[0][1]+100), font, 1,(255,255,255),2)

	cv2.imshow("Calibration",img)
	if(cv2.waitKey(1) & 0xFF == ord('n')):
		break
