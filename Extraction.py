import cv2
import numpy as np
import csv
import os
#from scipy import mode

#os.remove('HuMoments.csv')
#os.remove('RGB.csv')
#os.remove('MeanStdDev.csv')
#os.remove('ColorHist.csv')
class Extract(object):

	def ext(self,img,classnum):
		#Hu-moments Extraction
		gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
		blur = cv2.bilateralFilter(thresh,15,80,80)
		Humom=cv2.HuMoments(cv2.moments(blur)).flatten()
		#RGB Means extraction
		means = cv2.mean(img)
		means = means[:3]
		#Histogram extraction
		hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
		hist = hist.flatten()
		#Contour Hu
		gray2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		thresh=cv2.adaptiveThreshold(gray2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
		blur = cv2.bilateralFilter(thresh,15,80,80)
		gray_lap = cv2.Laplacian(blur,cv2.CV_16S,ksize = 3,scale = 1,delta = 0)
		dst = cv2.convertScaleAbs(gray_lap)
		Humom2=cv2.HuMoments(cv2.moments(dst)).flatten()
		'''
		#Mode
		most_intensity=mode(img)[0][0]
		'''
		#Stats Extraction
		(means2, stds) = cv2.meanStdDev(img)
		stats = np.concatenate([means2, stds]).flatten()
		#Class appending
		Humom=np.append(Humom,classnum)
		means=np.append(means,classnum)
		hist=np.append(hist,classnum)
		stats=np.append(stats,classnum)
		Humom2=np.append(Humom2,classnum)
		#most_intensity=np.append(most_intensity,classnum)
		
		with open('HuMoments.csv', 'ab')as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(Humom)
		'''
		with open('RGB.csv', 'ab')as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(means)
		'''
		with open('MeanStdDev.csv', 'ab')as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(stats)

		with open('ContourHu.csv', 'ab')as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(Humom2)
		'''
		with open('Mode.csv', 'ab')as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(most_intensity)
		'''
