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

cap=cv2.VideoCapture(1)

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

	cv2.imshow("Calibration",img)
	if(cv2.waitKey(1) & 0xFF == ord('n')):
		break
	'''
	A = img[boxA[0][1]:boxA[1][1], boxA[0][0]:boxA[1][0]]
	B = img[boxB[0][1]:boxB[1][1], boxB[0][0]:boxB[1][0]]
	C = img[boxC[0][1]:boxC[1][1], boxC[0][0]:boxC[1][0]]
	D = img[boxD[0][1]:boxD[1][1], boxD[0][0]:boxD[1][0]]

	'''
	A = img[box6[0][1]:box6[1][1], box6[0][0]:box6[1][0]]
	B = img[box5[0][1]:box5[1][1], box5[0][0]:box5[1][0]]
	C = img[box2[0][1]:box2[1][1], box2[0][0]:box2[1][0]]
	D = img[box1[0][1]:box1[1][1], box1[0][0]:box1[1][0]]
	
	resA = think2.detect(A)
	resB = think2.detect(B)
	resC = think2.detect(C)
	resD = think2.detect(D)

	if(0 == resA):
		if(0 == resB):
			if(0 == resD):
				print("Shelf is in center **first if**")
				cropimg[0]=img[box1[0][1]:box1[1][1], box1[0][0]:box1[1][0]]
				cropimg[1]=img[box2[0][1]:box2[1][1], box2[0][0]:box2[1][0]]
				cropimg[2]=img[box3[0][1]:box3[1][1], box3[0][0]:box3[1][0]]
				cropimg[3]=img[box4[0][1]:box4[1][1], box4[0][0]:box4[1][0]]
				cropimg[4]=img[box5[0][1]:box5[1][1], box5[0][0]:box5[1][0]]
				cropimg[5]=img[box6[0][1]:box6[1][1], box6[0][0]:box6[1][0]]
				for i in range (6):
					index[i][0]=cropimg[i]
					index[i][1]=think2.detect(cropimg[i])
				break
			else:
				print("Look Down")
		else:
			print("Look Right")
	elif(0 == resB):
		if(0 == resA):
			if(0 == resC):
				print("Shelf is in center **second if**")
				cropimg[0]=img[box1[0][1]:box1[1][1], box1[0][0]:box1[1][0]]
				cropimg[1]=img[box2[0][1]:box2[1][1], box2[0][0]:box2[1][0]]
				cropimg[2]=img[box3[0][1]:box3[1][1], box3[0][0]:box3[1][0]]
				cropimg[3]=img[box4[0][1]:box4[1][1], box4[0][0]:box4[1][0]]
				cropimg[4]=img[box5[0][1]:box5[1][1], box5[0][0]:box5[1][0]]
				cropimg[5]=img[box6[0][1]:box6[1][1], box6[0][0]:box6[1][0]]
				for i in range (6):
					index[i][0]=cropimg[i]
					index[i][1]=think2.detect(cropimg[i])
				break
			else:
				print("Look Down")
		else:
			print("Look Left")
	elif(0 == resC):
		if(0 == resD):
			if(0 == resB):
				print("Shelf is in center **third if**")
				cropimg[0]=img[box1[0][1]:box1[1][1], box1[0][0]:box1[1][0]]
				cropimg[1]=img[box2[0][1]:box2[1][1], box2[0][0]:box2[1][0]]
				cropimg[2]=img[box3[0][1]:box3[1][1], box3[0][0]:box3[1][0]]
				cropimg[3]=img[box4[0][1]:box4[1][1], box4[0][0]:box4[1][0]]
				cropimg[4]=img[box5[0][1]:box5[1][1], box5[0][0]:box5[1][0]]
				cropimg[5]=img[box6[0][1]:box6[1][1], box6[0][0]:box6[1][0]]
				for i in range (6):
					index[i][0]=cropimg[i]
					index[i][1]=think2.detect(cropimg[i])
				break
			else:
				print("Look Up")
		else:
			print("Look Right")
	elif(0 == resD):
		if(0 == resC):
			if(0 == resA):
				print("Shelf is in center **fourth if**")
				cropimg[0]=cropimg[box1[0][1]:box1[1][1], box1[0][0]:box1[1][0]]
				cropimg[1]=img[box2[0][1]:box2[1][1], box2[0][0]:box2[1][0]]
				cropimg[2]=img[box3[0][1]:box3[1][1], box3[0][0]:box3[1][0]]
				cropimg[3]=img[box4[0][1]:box4[1][1], box4[0][0]:box4[1][0]]
				cropimg[4]=img[box5[0][1]:box5[1][1], box5[0][0]:box5[1][0]]
				cropimg[5]=img[box6[0][1]:box6[1][1], box6[0][0]:box6[1][0]]
				for i in range (6):
					index[i][0]=cropimg[i]
					index[i][1]=think2.detect(cropimg[i])
				break
			else:
				print("Look Up")
		else:
			print("Look Left")
	else:
		print("Shelf not in vicinity! Look around!")

print index
for i in range(6):
	print "Cell ",i+1
	print index[i][1]
cv2.destroyAllWindows()
cap.release()
while(True):
	time.sleep(0.125)
	que=raw_input("What do you want to do? Track yellow/green/red? exit?")
	if(que == "yellow"):
		for i in range (6):
			if(index[i][1]==2):
				see.cam(index[i][0])
			else:
				print "No yellow container indexed"
	elif(que == "green"):
		for i in range (6):
			if(index[i][1]==3):
				see.cam(index[i][0])
			else:
				print "No Green container indexed"
	elif(que == "red"):
		for i in range (6):
			if(index[i][1]==4):
				see.cam(index[i][0])
			else:
				print "No Red container indexed"
	elif(que=="exit"):
		break

print "Program Succesfully terminated"
