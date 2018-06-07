# Sistema operativo  
FROM ubuntu:14.04  
# Autor  
MAINTAINER David Brao Serrano <dabrase@gmail.com>  
  
#Actualizar Sistema Base  
RUN sudo apt-get -y update  
  
# Instalacion  
RUN sudo apt-get install -y git  
RUN sudo git clone https://github.com/dabrase/proyectoIV  
  
#Instalar python  
RUN sudo apt-get -y install python-dev  
RUN sudo apt-get install -y python-setuptools  
RUN sudo apt-get install -y build-essential  
RUN sudo apt-get -y install libpq-dev  
RUN sudo easy_install pip  
RUN sudo pip install --upgrade pip  
  
# Instalacion de las dependencias del proyecto  
RUN cd proyectoIV/ && make install  

