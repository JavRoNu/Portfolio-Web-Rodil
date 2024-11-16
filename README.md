# Portofolio-Web-Rodil

Repo hosting [https://carlosrodil.com](https://carlosrodil.com)

[![Netlify Status](https://api.netlify.com/api/v1/badges/807748ce-5297-4f41-9f68-799fe958e4ca/deploy-status)](https://app.netlify.com/sites/carlosrodil/deploys)

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Netlify](https://img.shields.io/badge/netlify-%23000000.svg?style=for-the-badge&logo=netlify&logoColor=#00C7B7)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)

## Pyscripts

Pyhton3 scripts made for templating pages and processing web-images.

```bash
py (pyscript.py) arg1 arg2 .... 
```

- builpage.py: builds a project page with the template given. Takes into account projorder.txt to sort the projects within the next previous buttons.(calls cropAndresize.py or onlyresize.py if needed)
  - arg1:  project to build -> "media/(projid)"
  - arg2: only html, crop and resize, resize only -> empty,"cr","r"
- cropAndResize.py: crops and resizes project´s images to the desired width and height (dwidth l85,dheight l86) keeping the aspect ratio.
  - arg1:  project to build -> "media/(projid)"
- ResizeTHumb.py: resizes thumbnail given width and height.
  - arg1: file to tranform -> "media/(projid)/(projid)_thumb.jpg
  - arg2: desired min width -> 652
  - arg3: desired min height -> 366
- onlyresize.py: resize projects´s images to the desired width and height keeping the aspect ratio.
  - arg1:  project to build -> "media/(projid)"
- reparing.py: script made for projects or images that fail in the croping procces, uses alternative method.
  - arg1: id of the project -> "(id)"
- todalaweb.py: lists all projects in media and calls buildpage.py or ResizeThumb.py to rebuilt the whole projects section using the template contained in buildpage. Non exectuable design Ajdust variables thumb and html lines 17,18
- buildprojects.py: build the index page given the project order specified in projorder.txt

## Updating

- Add project folder with thumbnail, stills, and ``info.txt``
- Add project_id to ```pyscripts/projorder.txt``` in the desired position.
- Use ```ResizeThumb.py``` and delete original.
- Use ```buildpage.py``` with "cr" o "r" as de second argument.
- Remove old stills.
- If you dont want to rebuild the whole page with ```todalweb.py``` change previous and next links manually.
- Update the ```index.html``` with ```buildprojects.py```.
