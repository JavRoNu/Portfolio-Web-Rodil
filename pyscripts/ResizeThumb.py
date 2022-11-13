# script arguments 
# [1] the file to transform (char)
# [2] the min width (int)
# [3] the min heigth (int)

# modules
from posixpath import splitext
import cv2
import numpy as np
import os
import sys

# read image get the shape
elfile = sys.argv[1]

print("Working in "+ elfile)
splited = os.path.splitext(elfile)

image = cv2.imread(elfile)

im_h,im_w = image.shape[:2]

# check for min  width and heights
if len(sys.argv) < 3:
    dwidth = int(input("Min Width:"))
else:
    dwidth = int(sys.argv[2])

if len(sys.argv) < 4:
    dheight = int(input("Min Height:"))
else:
    dheight = int(sys.argv[3])
    
# maximum reduction available
redus = np.flip(np.arange(start=1,stop=4.1,step=.1))

wre = im_w/redus
hre = im_h/redus 

okwidth = np.amin(np.where(wre > dwidth))
okheight = np.amin(np.where(hre > dheight))

reduction = np.amax(np.array([okwidth,okheight]))
reduction = redus[reduction]

# resize and save
final_w = round(im_w/reduction)
final_h = round(im_h/reduction)

print("Final size: "+str(final_w)+" x "+str(final_h))        

rs_img = cv2.resize(image,(final_w,final_h))

cv2.imwrite(splited[0]+"_res"+splited[1],rs_img,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
print("Thumbnail completed !!")
    