FROM ubuntu:14.04  
MAINTAINER Roberto Rosario "roberto.rosario@mayan-edms.com"  
RUN apt-get -qq update  
RUN apt-get install python-dev python-pip tesseract-ocr unpaper tesseract-ocr
libreoffice ghostscript libjpeg-dev libpng-dev libtiff-dev poppler-utils
supervisor -y  
RUN pip install mayan-edms==1.1.0  
RUN mayan-edms.py syncdb --migrate --noinput  
EXPOSE 8000  
CMD mayan-edms.py runserver 0.0.0.0:8000  

