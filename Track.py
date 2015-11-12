import numpy as np
import cv2

class Eye(object):
	def cam(self,cap1):

    		cap = cv2.VideoCapture(0)

    		ret,frame = cap.read()
    		roi=cap1

    		hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    		mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    		roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
    		cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

	# Setup the termination criteria, either 10 iteration or move by at least 1 pt
    		term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

    		while(1):
        		ret ,frame = cap.read()
    
        		if ret == True:
            			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            			dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        
            # camshift
            			ret, track_window = cv2.CamShift(dst, track_window, term_crit)
            # Draw it on image
            			pts = cv2.cv.BoxPoints(ret)
            			pts = np.int0(pts)
            			cv2.polylines(frame,[pts],True, 255,2)
            			img2=frame
            			cv2.imshow('Sight',img2)
        
            			k = cv2.waitKey(60) & 0xff
            			if k == 27:
                			break
            			else:
                			cv2.imwrite(chr(k)+".jpg",img2)

        		else:
            			break

    		cv2.destroyAllWindows()
    		cap.release()
