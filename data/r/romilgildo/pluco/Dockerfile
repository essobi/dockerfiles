# Sistema operativo  
FROM ubuntu:14.04  
# Autor  
MAINTAINER Ruben Martin Hidalgo <rubenmartin1991@gmail.com>  
  
# Instalacion de paquetes basicos  
RUN sudo apt-get update  
RUN sudo apt-get install -y git  
RUN sudo apt-get install -y build-essential  
  
# Descarga repositorio de la app  
RUN sudo git clone https://github.com/romilgildo/IV-PLUCO-RMH.git  
  
# Instalacion de la app y sus dependencias  
RUN cd IV-PLUCO-RMH && git pull  
RUN cd IV-PLUCO-RMH && make install  

