
# Librerías

import cv2
import numpy as np
import os
import sys

# variables de entorno
eldir = sys.argv[1]

if eldir.endswith("/") != True:
    eldir = eldir + "/"

losfiles = os.listdir(eldir)
print(losfiles)

for i in losfiles:
    
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
        
        # errores con el tema del RGB Y BGR

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)            
        _, thresh = cv2.threshold(gray, crlimit, 255, cv2.THRESH_BINARY)

        # extraer bordes simples
        contours, hierarchy = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        thisone = -1

        for i in range(0,len(contours)):
            newarea = cv2.contourArea(contours[i])
            if newarea/totarea > 0.5: thisone = i
     
        cnt = contours[thisone]
        x, y, w, h = cv2.boundingRect(cnt)

        # check if is ok
        newarea = cv2.contourArea(contours[thisone])
        if newarea/totarea < 0.5:
            crlimit = crlimit + 1
        else:
            exit = True 
        
        
    # cropping con np
    crop = image[y+8:y+h-8, x+8:x+w-8]

    # guardar el cropeo al 100%
    cv2.imwrite(thefile2[0]+"_cro"+thefile2[1], crop,[cv2.IMWRITE_JPEG_QUALITY, 100])
    
    im_h,im_w = crop.shape[:2]

    dwidth = 416
    dheight = 234
        
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
    cv2.imwrite(thefile2[0]+"_cro_th"+thefile2[1],rs_crop,[cv2.IMWRITE_JPEG_QUALITY, 100])


print("All done!!")