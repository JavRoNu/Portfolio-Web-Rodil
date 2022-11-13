import cv2
import os 
import sys
import re
import numpy as np
import matplotlib.pyplot as plt


eldir = "media/" + sys.argv[1]

#eldir = "media/afternoon"
if eldir.endswith("/") != True:
    eldir = eldir + "/"

allfiles = os.listdir(eldir)

p = re.compile("[0-9]{1,2}.jpg$")

losfiles = [ i for i in allfiles if p.search(i) ]

abc = "\n".join(losfiles)
numbers = re.findall("[0-9]{1,2}",abc)
numbers = [int(i) for i in numbers]
position = sorted(range(len(numbers)),key=numbers.__getitem__)
losfiles2 =  [losfiles[i] for i in position]

thefile = eldir + losfiles2[0]
img = cv2.imread(thefile)

# extraer bordes simples
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

arecont = list()
for i in range(0,len(contours)):
    newarea = cv2.contourArea(contours[i])
    arecont.append(int(newarea))

cntindex = arecont.index(max(arecont))


x, y, w, h = cv2.boundingRect(contours[cntindex])
print(x,y,w,h)
for i in losfiles2:
    
    thefile = eldir + i
    print("Trabajando en "+ thefile)
    thefile2 = list(os.path.splitext(thefile))
    
    image = cv2.imread(thefile)
    print(image.shape[:2])
    print(type(image))
    crop = image[y:y+h, x:x+w]
    print(type(crop))
    

    # guardar el cropeo al 100%
    #cv2.imwrite(thefile2[0]+"_cro"+thefile2[1], crop,[cv2.IMWRITE_JPEG_QUALITY, 100])
    print(crop.shape[:2])
    im_h,im_w = crop.shape[:2]

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

    rs_crop = cv2.resize(crop,(final_w,final_h))
    cv2.imwrite(thefile2[0]+"_cror"+thefile2[1],rs_crop,[cv2.IMWRITE_JPEG_QUALITY, 100])