# Portofolio-Web-Rodil

Repo hosting [https://carlosrodil.com](https://carlosrodil.com)

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
- onlyresize.py: rresize projects´s iamges to the desired width and height keeping the aspect ratio.
  - arg1:  project to build -> "media/(projid)"
- reparing.py: script made for projects or images that fail in the croping procces, uses alternative method.
  - arg1: id of the project -> "(id)"
- todalaweb.py: lists all projects in media and calls buildpage.py or ResizeThumb.py to rebuilt the whole projects section using the template contained in buildpage. Non exectuable design Ajdust variables thumb and html lines 17,18
