									Object detection and tracking using ML and camShift


	Phase I:	Start the training process with "Trainer.py".
	Phase II:	Then start object detection and tracking with "Tester.py"

												Phase I 

1. Trainer.py
	
	Shelf Training 

	-> Enter the ingredients contained in the yellow, green and red container.
	-> A simple imshow window runs under the name "Shelf training".
	-> Press 'C' or 'c' to start the shelf training. This will show a rectangle drawn on the video stream.
	-> Bring the shelf inside the drawn rectangle and press 'S' or 's' to extract features of shelf. [Class 0]
	-> Remove the shelf from within the rectangle and press 'D' or 'd' to extract features of background.(Anything without the shelf) [Class 1]
	-> Once the above two steps are done press 'Q' or 'q' to quit shelf training.

	Container Training

	-> A new imshow window opens under the name "Container training".
	-> Press 'C' or 'c' to start container training. This will show a smaller rectangle drawn on the video stream.
	-> Bring the containers one at a time within the rectangle and press 'Y' or 'y' for a yellow container, 'G' or 'g' for a green container, 'R' or 'r' for a red container. [Class 2,3,4]
	-> This will extract features according to the class. (Take care to press keys appropriately).
	-> Once the above steps are done press 'Q' or 'q' to quit container training.

2. Extraction.py
	
	Any image sent to the ext() function inside the Extract class will have the following features extracted and save in the corresponding files:
		
		-> Hu-moments		-	HuMoments.csv
		-> RGB Means		-	RGB.csv
		-> Mean and std.Devs	-	MeanStdDev.csv


												Phase II

3. Tester.py

	-> When the program starts, an imshow window opens with a 2 x 3 grid (labelled UL UR ML MR LL and LR in program as comments where U:UPPER M:MIDDLE L:LOWER AND L:LEFT R:RIGHT)
	-> The LL, LR, UR and UR grids also have a smaller box within (labelled as A B C and D respectively in program as comments)
	-> Each of the image inside A, B, C and D are sent to Bay.py to check if it has an image of the shelf or not and the user is directed accordingly 
	  so that all four corners have an image of the shelf. [Class 0]
	-> Once all four corners have images of the shelf, Images from each of the grid are sent to Bay.py to detect and return what image is what.
	-> Each image is indexed to it's appropriate class.
	-> Then the user can input which of the class he wants to track and the particular image is sent to Track.py which runs the camShift function.
	-> User can press 'Esc' to quit the camShift function and return to Tester.py
	-> Type 'exit to quit Tester.py

4. Bay.py

	-> Each column in the feature files are read and seperated according to the class they belong to.
	-> Mean and Standard deviation in each column is calculated for each of the class.
	-> Respective features are extracted from the numpy array (image) passed as input.
	-> Gaussian equation calculates the conditional probability for the input feature(x) with respect to the means and standard deviations and returns the
	   probability for that particular feature to belong to each of the class.
	-> The maximum probablity is chosen as the appropriate class the image belongs to in that feature file.
	-> The Above steps are done in each of the extracted features from Extraction.py and a class is predicted.
	-> The final class the image belongs to is chosen as the maximum of the output from each of the features.
			For example, if an input image is predicted as class 2 from HuMomnets.csv, class 2 from RGB.csv and class 3 from MeanStdDev.csv then the image is classified as class 2 (Yellow container)

5. Track.py

	-> An imshow window named "Sight" opens and the input numpy array(image) from Tester.py is passed as input to the function cam().
	-> camShift function over the live streaming video is run with the input image as argument.
	-> A bounding box is drawn over the image in the video if the image exists in the live stream.
	-> User can click 'Esc' to quit the program and return to Tester.py
