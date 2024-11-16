
import os
import re 

# toma como base el directorio de ejcución
# recuerda adaptar rutas en os.system(...


# solo los proyectos que esten en ejecución
orden = open("./pyscripts/projorder.txt","r",encoding="utf-8")

orden = orden.readlines()

orden = [s.rstrip("\n") for s in orden]

thumb = False
html = True

# no funciona por que se ñadieron formatos nuevos png jpeg
if thumb == True:
    print("Creating thumbnails")
    for i in orden:
        print("Working on "+i)
        inside = "media/"+ i + "/"+i+"_thumb.jpg"
        os.system("/pyscripts/ResizeThumb.py " + inside + " 652 366")
    print("All thumbnails completed")


if html == True:    
    print("Rebuilding htmls")
    for i in orden: 
        inside = "media\\"+ i  
        print("\n----------------------\n")
        os.system("pyscripts\\buildpage.py  " + inside )
    print("All project pages completed!")
