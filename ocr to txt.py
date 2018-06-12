#                                            PYTHON CODE FOR OCR AND SAVING INTO TEXT FILE:



from PIL import Image
import pytesseract
import argparse
import cv2
import os
directory = os.path.join("folder path for image")
for root,dirs,files in os.walk(directory):
	ap = argparse.ArgumentParser()
	ap.add_argument("-i","--image",required = True,help="")
	ap.add_argument("-p","--preprocess",type=str,default="thresh",help="")
	args = vars(ap.parse_args())
	image = cv2.imread(args["image"])
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	if args["preprocess"] == "thresh":
		gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	elif args["preprocess"] == "blur":
		gray = cv2.medianBlur(gray,3)
	filename = "{}.jpg".format(os.getpid())
	cv2.imwrite(filename,gray)
	text = pytesseract.image_to_string(Image.open(filename))
	with open(directory+"\\"+"k"+".txt",'w') as f: f.write(str(text))
# os.system('espeak -f 'folder path'')  #optional only to convert the text to speech
os.remove(filename)

cv2.imshow("Image",image)   #optional to show image 
cv2.imshow("Output",gray)   #optional to show gray scale image
cv2.waitKey(0)
