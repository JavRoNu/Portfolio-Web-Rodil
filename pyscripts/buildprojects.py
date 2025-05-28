import os
import re
import codecs

# solo los proyectos que esten en ejecución
orden = open("./pyscripts/projorder.txt","r",encoding="utf-8")

orden = orden.readlines()

orden = [s.rstrip("\n") for s in orden]

# html template loop


oneproje = '''
  <div class = "col-md p-2" >
    <div class="img-ho img_wrap_c ratio ratio-16x9">
      <img src="{0}" class = "img-fluid">
      <a href="projects/{1}.html"> 
        <div class="img_description_wht">
          <p class = "fs-5">{2}</p>
          <p class = "fs-6 fst-italic">{3}</p>
        </div>
      </a>
    </div>
  </div>
'''



allproj = list()

for i in orden:
    
    files = os.listdir("./media/"+i)

    p = re.compile('thumb')

    thethumb = [k for k in files if p.findall(k)]
    thethumb = "./media/"+i+"/"+thethumb[0]
    
    info = open("./media/"+i+"/info.txt", "r",encoding="utf-8")
    info = info.readlines()
    keep = list()
    
    for y in info:
        if y != "\n": keep.append(y)

        end = "".join(keep)
        end = re.findall('["-]{1}(.*?)["\\n]{1}',end)
    # extraer datos de .txt
    
    titulo,tipo = [end[x] for x in [1,2]]
    
    allproj.append(oneproje.format(thethumb,i,titulo,tipo)) 

allproj = "\n".join(allproj)


head = '''
<!DOCTYPE html>
<html lang = "en">
  <head>
      <meta charset="UTF-8">
      <META HTTP-EQUIV = "X-UA-<!doctype html">
      <meta name= "viewport" content="width=device-width, initial-scale=1.0">
      <meta name="description" content="">
      <title>Carlos Rodil Cinematographer</title>

      <link rel="apple-touch-icon" sizes="180x180" href="iconos/apple-touch-icon.png">
      <link rel="icon" type="image/png" sizes="32x32" href="iconos/favicon-32x32.png">
      <link rel="icon" type="image/png" sizes="16x16" href="iconos/favicon-16x16.png">

            <!--Bootrap 5 descargado y en el repo 
      <link rel="stylesheet" href="bootstrap-5.0.2-dist/css/bootstrap.min.css"/>
      <script src="bootstrap-5.0.2-dist/js/bootstrap.min.js"></script> -->

      <!--Bootstrap 5 CDN-->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

      <!-- Mis estilos aparte -->
      <link rel="stylesheet" href="miestilo.css">

      <!-- Lo de fontAwesome -->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  </head>
  <body id = "lgrad">

    <!-- Barra de navegación superior-->
    <!--<nav class="navbar navbar-light navbar-expand-sm">  el anterior -->
      <nav class ="navbar sticky-top navbar-light navbar-expand-sm">
        <div class="container-fluid">
          <div class="navbar-brand ms-md-5 mt-1">
            <img src="media/rodilogo1_low_gray_pl2.svg" alt="" class="img-fluid" id = "mainlogo">
          </div>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto pe-md-5">
              <li class="nav-item">
                <a class="nav-link navsec" href=# id = "activenavlink3">PROJECTS</a>
              </li>
              <li class="nav-item">
                <a class="nav-link navsec" href="reel.html">REEL</a>
              </li>
              <li class="nav-item">
                <a class="nav-link navsec" href="about.html">CONTACT</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    <div class="container-lg pt-5 d-flex justify-content-center visually-hidden" id = "navproje">
        <div class="btn-group btn-group-sm fs-5" role="group" aria-label="...">
            <button class="button mx-4 px-4" id="projall"onclick="filterproj('All')">All</button>
            <button class="button mx-4 px-4" id="projcom"onclick="filterproj('Commercial')">Commercial</button>
             </div>
            <div class="btn-group btn-group-sm fs-5" role="group" aria-label="...">   
            <button class="button mx-4 px-4" id="projnar" onclick="filterproj('Narrative')">Narrative</button>
            <button class="button mx-4 px-4" id="projmus"onclick="filterproj('Music')">Music video</button>
        </div>
    </div>

     <!---Grid dos columnas para proyectos-->
     <div class = "container-lg pt-5 mt-2 px-4">
      <div class="row row-cols-md-3 row-cols-lg-3 d-flex flex-wrap align-items-center"  id ="projsec">
'''

tail = '''
 </div>
</div>
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
        href="https://www.imdb.com/name/nm7492357/"
           role="button" ><i class="fab fa-imdb"></i>
        </a>
        </div>
      </div>
    </div>
    <!-- Footer con registro -->
  <div class="container-fluid d-flex aligns-items-center justify-content-center pb-5 pt-3">
    <p id ="elcopy">©2024</p>
  </div>

    <!--Para la libreria de animación con scroll-->
    <!--
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
    <script>
      AOS.init();
    </script>
  -->  

          <!-- Funciones propias en js de modificación etc -->
          <script src="mijava.js"></script>

      
  </body>
</html>
'''
    
allin = [head,allproj,tail]
allin = "\n".join(allin)

# crear o abrir HTML y escribir
Func = codecs.open("./index.html","w","utf-8")
Func.write(allin)
Func.close()

# print final
print("HTML index page completed in main folder!!")
   
    