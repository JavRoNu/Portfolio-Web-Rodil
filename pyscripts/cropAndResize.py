
# Librerías

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

p = re.compile("[0-9]{1,2}(.jpg|.png|.jpeg)$")

losfiles = [ s for s in allfiles if p.search(s) ]

print(losfiles)

for i in losfiles:
    
    gocrop = True
    thefile = eldir + i
    print("Trabajando en "+ thefile)
    thefile2 = list(os.path.splitext(thefile))

    img = cv2.imread(thefile)

    # Borde negro por seguridad
    image = cv2.copyMakeBorder(img, 100, 100, 100, 100,
                            cv2.BORDER_CONSTANT, None, value=0)

    # a gris y lo del threshold binario
    crlimit = 1
    totarea = image.shape[0] * image.shape[1]
    exit = False

    while exit == False:
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, crlimit, 255, cv2.THRESH_BINARY)

        # extraer bordes simples
        contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        thisone = -1
        
        # si detecta contours
        if len(contours) > 0 & crlimit < 11:
            
            for i in range(0, len(contours)):
                newarea = cv2.contourArea(contours[i])
                if newarea/totarea > 0.5:
                    thisone = i
        
            cnt = contours[thisone]
            x, y, w, h = cv2.boundingRect(cnt)

            # check if is ok
            newarea = cv2.contourArea(contours[thisone])
            if newarea/totarea < 0.5:
                crlimit = crlimit + 1
            else:
                exit = True
        else:
            exit = True
            gocrop = False
            print("ALERTA!!: No se detectaron contours para: "+thefile)
        
        
    if gocrop:    
        # cropping con np
        crop = image[y+8:y+h-8, x+8:x+w-8]

        # guardar el cropeo al 100%
        cv2.imwrite(thefile2[0]+"_cro"+thefile2[1], crop,[cv2.IMWRITE_JPEG_QUALITY, 100])
        
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


print("All done!!")