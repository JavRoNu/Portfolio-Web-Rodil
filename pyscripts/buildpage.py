
import os
import sys
import re
import codecs

# variables de entorno
eldir = sys.argv[1]

#if eldir.endswith("/") != True:
#    eldir = eldir + "/"

allfiles = os.listdir(eldir)

print("Working on " + eldir)

# mirar la info en info.txt
p = re.compile(".txt$")
lainfotxt = [ s for s in allfiles if p.search(s) ]
lainfotxt = str(lainfotxt[0])

#### check for secondary argument for croping and resizing images ####
if len(sys.argv) < 3 :
    print("Only rebuilding html")
else:
    if sys.argv[2] == "cr":
        print("Building html with crop and resize")
        os.system("cropAndResize.py "+ eldir )
        
    elif sys.argv[2] == "r":
        print("Building hmtl with resize")
        os.system("onlyresize.py "+ eldir )
    else:
        raise NameError('El tipo de procesado es incorrecto, validos:(cr,r)')

#### html templating ####

file = open(eldir+"/"+lainfotxt, "r",encoding="utf-8")

file = file.readlines()

#selecionar solo las distintas a \n
keep = list()
for i in file:
    if i != "\n": keep.append(i)

end = "".join(keep)
#print(end)
end = re.findall('["-]{1}(.*?)["\\n]{1}',end)

# extraer datos de .txt
id,titulo,tipo,url = [end[i] for i in range(4)]
camera = end[len(end)-1]

# url a vimeoid number
vimeoid = re.findall("[0-9]{1,99}",url)
vimeoid = str(vimeoid[0])

# Informacion adicional en lista
adinfo = [end[i] for i in range(4,len(end)-1)]

for i in range(0,len(adinfo)):
    elstr = adinfo[i]
    if elstr.startswith("-"):
        adinfo[i] = elstr[1:].strip()
    else:
        adinfo[i] = elstr.strip()
        
listainfo = list()

for i in range(0,len(adinfo)):
  go = adinfo[i].split(":")
  go = go[0]+": "+'<span class = "fw-bold">'+go[1]+ "</span>"
  listainfo.append("<li>"+go+"</li>")

listainfo = "".join(listainfo)

# screens del proyecto 
fotos = os.listdir(eldir)
p = re.compile("[0-9]{1,2}_cror.jpg$")
lasfotos = [ s for s in fotos if p.search(s) ]

# ordenando por número
lasfotos2 = "\n".join(lasfotos)
numbers = re.findall("[0-9]{1,2}",lasfotos2)
numbers = [int(i) for i in numbers]

position = sorted(range(len(numbers)),key=numbers.__getitem__)

lasfotos =  [lasfotos[i] for i in position]

# <div class = "col-md p-3" data-aos="fade-up">
singlepic = """
          <div class = "col-md p-3">
            <img src="{0}"class = "img-fluid" loading="lazy">
          </div> 
"""
htmlfotos = list()

for i in range(0,len(lasfotos)):
     htmlfotos.append(singlepic.format("../media/"+id+"/"+lasfotos[i]))
    
htmlfotos = "".join(htmlfotos)


# BOTONES PREVIOUS NEXT
orden = open("./pyscripts/projorder.txt","r",encoding="utf-8")

orden = orden.readlines()

orden = [s.rstrip("\n") for s in orden]

orderpos = orden.index(id)

prev = orderpos -1
next = orderpos + 1

if prev <= 0:
    prev = """
      <div class="container-lg pt-3" id = "prenext">
        <div class="d-flex justify-content-center">
        <a class="btn btn-white dissabled"
            href="#"
            role="button">< PREV
        </a>
    """
else:
    prev = """
      <div class="container-lg pt-3" id = "prenext">
        <div class="d-flex justify-content-center">
        <a class="btn btn-white"
            href="{0}.html"
            role="button">< PREV
        </a>
    """
    prev = prev.format(orden[orderpos-1])
    
    
if next >= len(orden):
    next = """
          <a class=" btn btn-white disabled"
            href="#" 
            role="button">NEXT >
          </a>
        </div>
      </div>
    """
else:
    next = """
          <a class=" btn btn-white"
            href="{0}.html" 
            role="button">NEXT >
          </a>
        </div>
      </div>
    """
    next = next.format(orden[orderpos+1])


    

# BLOQUES HTML
header = """<!DOCTYPE html>
<html lang = "en">
  <head>
      <meta charset="UTF-8">
      <META HTTP-EQUIV = "X-UA-<!doctype html">
      <meta name= "viewport" content="width=device-width, initial-scale=1.0">
      <meta name="description" content="">
      <title>Carlos Rodil Cinematographer</title>
      
      <link rel="icon" type="image/png" sizes="32x32" href="iconos/CR_favicon.png">

      <!--Bootrap 5 descargado y en el repo 
      <link rel="stylesheet" href="bootstrap-5.0.2-dist/css/bootstrap.min.css"/>
      <script src="bootstrap-5.0.2-dist/js/bootstrap.min.js"></script> -->

      <!--Bootstrap 5 CDN-->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

      <!-- Mis estilos aparte -->
      <link rel="stylesheet" href="../miestilo.css">

      <!-- Lo de fontAwesome -->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
      
  </head>
  <body id = "lgrad">

    <!-- Barra de navegación superior-->
    <nav class="navbar sticky-top navbar-light navbar-expand-sm">
        <div class="container-fluid">
          <a class="navbar-brand ms-md-5 mt-1"href="href="www.carlsorodil.com">
            <img src="../media/rodilogo1_low_gray_pl.svg" alt="" class="img-fluid" id = "mainlogo">
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto pe-md-5">
              <li class="nav-item">
                <a class="nav-link navsec" href="../allprojects.html">PROJECTS</a>
              </li>
              <li class="nav-item">
                <a class="nav-link navsec" href="../reel.html">REEL</a>
              </li>
              <li class="nav-item">
                <a class="nav-link navsec" href="../about.html">ABOUT</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>"""
      
formatinfo = """
    <!--Jumbotron superior-->
    <div class="container-lg pt-5 mt-2" id ="jtcontainer">
        <div class="ratio ratio-16x9 shadow">
            <iframe src="https://player.vimeo.com/video/{0}?autoplay=0&loop=1&muted=0&portrait=0" frameborder="0"
              allow="fullscreen"  allowfullscreen></iframe>
        </div>
    </div>
    <!-- info relevante -->
    <div class="container-lg pb-1 pt-5 pl-3 pr-3">
        <div class="text-start ml-2">
            <div class="fs-4 fw-bold">
            {1} 
            </div>
            <div class = "pb-2 fst-italic">
            {2}
            </div>
            <ul class="list-unstyled pb-2">
            {3}
            </ul>
            <div>
            {4}
            </div>
            
        </div>
    </div>
    <!-- Zona imagenes -->
      <div class="container-lg pt-5">
        <div class="row row-cols-md-2 row-cols-lg-2 d-flex flex-wrap align-items-center">
        {5}
        </div>
      </div>"""
      
      
footer = """
      <!-- Footer con RRSS -->
      <div class="container-lg pt-5 mt-5 pb-2" id="misredes">
        <div class="d-flex justify-content-center">
          <div id = "gogo">
            <a class="shadow btn btn-white"
              href="https://vimeo.com/carlosrodil"
              role="button"><i class="fab fa-vimeo-v"></i>
            </a>
            <a class="shadow btn btn-white mx-4"
              href="https://www.instagram.com/carlos.rodil_/" 
              role="button"><i class="fab fa-instagram"></i>
            </a>
              <a class="shadow btn btn-white"
                onclick = "showCP()"
                role="button"><i class="fab fa-imdb"></i>
              </a>
          </div>
        </div>
      </div>
      <div class="container-sm d-flex justify-content-center visually-hidden" id = "colorpanel">
          <div class="row" style="max-width: 350px;">
                <label for="colorfondo">Seleccione color de fondo:</label>
                <input type="color" id="colorfondo" name="colorfondo" value="#ffffff" onchange="changeCOL()">
                <p id = "colorhex">Codigo HEX:</p>
                <p>Recuerde que puede volver a pulsar el boton de imdb para ocultar este menu</p>
          </div>
      </div>
  
      <!-- Footer con registro -->
    <div class="container-fluid d-flex aligns-items-center justify-content-center pb-5 pt-3">
      <p id ="elcopy">©2022 Carlos Rodil . All rights reserved. No part of this website may be reproduced without permission.</p>
    </div>
            <!-- Funciones propias en js de modificación etc -->
            <script src="../mijava.js"></script>

 </body>
</html>"""


# Hacer el formating y juntar todo 
formatinfo = formatinfo.format(vimeoid,titulo,tipo,listainfo,camera,htmlfotos)
allin = [header,formatinfo,prev,next,footer]
allin = "\n".join(allin)

# crear o abrir HTML y escribir
Func = codecs.open("projects/"+id+".html","w","utf-8")
Func.write(allin)
Func.close()

# print final
print("HTML page completed in "+"projects/"+id+".html")
