FROM ubuntu:latest  
  
#Autor  
MAINTAINER Antonio Miguel Pozo Cámara <antoniopozo26@gmail.com>  
  
#Actualizar  
RUN sudo apt-get update  
  
#Descargar aplicación  
RUN sudo apt-get install -y git  
RUN sudo git clone https://github.com/AntonioPozo/Bares.git  
  
#Instalacíon software necesario  
RUN sudo apt-get install -y python-setuptools  
RUN sudo apt-get -y install python-dev  
RUN sudo apt-get -y install build-essential  
RUN sudo easy_install pip  
RUN sudo pip install --upgrade pip  
  
RUN sudo apt-get build-dep python-imaging -y  
RUN sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
-y  
  
#Instalo dependencias  
RUN cd Bares/ && sudo pip install -r requirements.txt  
  

