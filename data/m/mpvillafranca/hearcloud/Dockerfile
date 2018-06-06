FROM ubuntu:latest  
  
#Autor  
MAINTAINER Mariano Palomo Villafranca <mpvillafranca@correo.ugr.es>  
  
#Actualizar el sistema  
RUN sudo apt-get -y update  
  
#Instalar git y descargar la aplicacion  
RUN sudo apt-get install -y git  
RUN sudo git clone https://github.com/mpvillafranca/hear-cloud.git  
  
# Instalar Python y PostgreSQL  
RUN sudo apt-get install -y python-setuptools  
RUN sudo apt-get -y install python-dev  
RUN sudo apt-get -y install build-essential  
RUN sudo apt-get -y install python-psycopg2  
RUN sudo apt-get -y install libpq-dev  
RUN sudo easy_install pip  
RUN sudo pip install --upgrade pip  
  
#Instalamos las dependencias y la aplicacion  
RUN cd hear-cloud/ && sudo pip install -r requirements.txt  
  
#Realizamos migraciones  
RUN cd hear-cloud/ && python manage.py syncdb --noinput  

