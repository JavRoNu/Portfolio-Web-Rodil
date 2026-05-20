
#!/usr/bin/env python3  
import sys
import os
import re
import subprocess

# Bandera global para controlar si hubo fallos en el proceso
exception_occurred = False

try:
    with open("./pyscripts/projorder.txt", "r", encoding="utf-8") as f:
        orden = [line.rstrip("\n") for line in f.readlines()]
except FileNotFoundError:
    print("Error: No se encontró el archivo projorder.txt")
    sys.exit(1)

cwd = os.getcwd()
print(f"Directorio actual: {cwd}")

findthumb = re.compile("_(thumb)\.(jpg|jpeg|png|bmp|tiff|svg)$", re.IGNORECASE)
findold = re.compile("_[0-9]{1,2}(_cro)?\.(jpg|jpeg|png|bmp|tiff|svg)$", re.IGNORECASE)

for i in orden:
    # exo indica si el proyecto actual falló
    exo = False
    media_path = f"./media/{i}"
    
    if not os.path.exists(media_path):
        print(f"Error: No existe la carpeta {media_path}")
        exception_occurred = True
        continue

    projfiles = os.listdir(media_path)
    thumbname = [s for s in projfiles if findthumb.search(s)]
    
    # 1. Recortar y redimensionar imágenes generales
    res_crop = subprocess.run(['py', f'{cwd}/pyscripts/cropAndResize.py', f'{cwd}/media/{i}', 'cr'], check=True)
    if res_crop.returncode != 0:
        exo = True
        exception_occurred = True
        print(f"Error al recortar/redimensionar en proyecto {i}")
    
    # 2. Procesar miniatura si existe
    if thumbname:
        thumb_file = f"{cwd}/media/{i}/{thumbname[0]}"
        res_thumb = subprocess.run(['py', f'{cwd}/pyscripts/ResizeThumb.py', f'{cwd}/media/{i}/{thumbname[0]}', '652', '366'], check=True)
        if res_thumb.returncode != 0:
            exo = True
            exception_occurred = True
            print(f"Error al redimensionar miniatura para {i}")
    else:
        print(f"No se encontró miniatura para {i}")
        exo = True
        exception_occurred = True
    
    # 3. Limpieza de archivos si todo salió bien para este proyecto
    if not exo:
        projfiles = os.listdir(media_path)
        borra = [s for s in projfiles if findold.search(s)]
        borra.append(thumbname[0])                      
        for i2 in borra:
            try:
                os.remove(f"{media_path}/{i2}")
            except OSError as e:
                print(f"No se pudo eliminar {i2}: {e}")

# 4. Construcción final 
res_build = subprocess.run(['py', f'{cwd}/pyscripts/buildprojects.py'])
if res_build.returncode != 0:
    print("Error al construir la página principal de proyectos.")
