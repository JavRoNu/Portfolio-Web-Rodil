
import os
import re 

# toma como base el directorio de ejcución
# recuerda adaptar rutas en os.system(...
mediapro = os.listdir("media")
p = re.compile(".jpeg$")

losfiles = [ i for i in mediapro if not p.search(i) ]

p = re.compile(".svg$")

losfiles = [ i for i in losfiles if not p.search(i) ]


thumb = False
html = True

if thumb == True:
    print("Creating thumbnails")
    for i in losfiles:
        print("Working on "+i)
        inside = "media/"+ i + "/"+i+"_thumb.jpg"
        os.system("/pyscripts/ResizeThumb.py " + inside + " 652 366")
    print("All thumbnails completed")


if html == True:    
    print("Rebuilding htmls")
    for i in losfiles: 
        inside = "media\\"+ i  
        print("\n----------------------\n")
        os.system("pyscripts\\buildpage.py  " + inside )
    print("All project pages completed!")
