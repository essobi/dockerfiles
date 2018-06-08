FROM ubuntu:latest  
  
#Autor  
MAINTAINER Jose Ignacio Recuerda Cambil <ignacio.recuerda@gmail.com>  
  
#Actualizar  
RUN sudo apt-get update  
  
#Descargar aplicación  
RUN sudo apt-get install -y git  
RUN sudo git clone
https://github.com/ignaciorecuerda/gestionpedidos_django.git  
  
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
RUN ls gestionpedidos_django/  
RUN cd gestionpedidos_django/ && sudo pip install -r requirements.txt

