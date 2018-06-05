# Sistema Operativo  
FROM ubuntu:latest  
  
# Autor  
MAINTAINER Gabriel Stan  
  
# Preparacion del contenedor  
# RUN apt-get clean  
RUN apt-get update  
RUN apt-get install -y git build-essential make sudo  
  
# Descarga del repositorio y preparacion de la aplicacion  
RUN git clone -b BACKEND-1 --single-branch https://github.com/gabriel-
stan/gestion-tfg.git  
  
RUN cd gestion-tfg && make install_basic  
  
# Comando para lanzar la aplicacion  
CMD cd gestion-tfg && make run_gunicorn  

