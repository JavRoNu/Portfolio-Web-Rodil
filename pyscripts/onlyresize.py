import cv2
import numpy as np
import os
import sys
import re

# variables de entorno
eldir = sys.argv[1]

if eldir.endswith("/") != True:
    eldir = eldir + "/"

allfiles = os.listdir(eldir)

p = re.compile("[0-9]{1,2}.jpg$")

losfiles = [ s for s in allfiles if p.search(s) ]

print(losfiles)

for i in losfiles:
    
    thefile = eldir + i
    print("Trabajando en "+ thefile)
    thefile2 = list(os.path.splitext(thefile))

    img = cv2.imread(thefile)
    
    im_h,im_w = img.shape[:2]

    dwidth = 652
    dheight = 366
        
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

    rs_crop = cv2.resize(img,(final_w,final_h))
    cv2.imwrite(thefile2[0]+"_cror"+thefile2[1],rs_crop,[cv2.IMWRITE_JPEG_QUALITY, 100])