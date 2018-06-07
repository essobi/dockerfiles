FROM ubuntu:latest  
  
#Autor  
MAINTAINER Samuel Carmona Soria <samuelcarmona123@gmail.com>  
  
#Actualizar Sistema Base  
RUN sudo apt-get update  
#Descargar aplicacion  
RUN sudo apt-get install -y git  
RUN sudo git clone https://github.com/Samuc/Proyecto-IV-modulo3  
  
#Instalar paquetes necesarios  
RUN sudo apt-get install -y python-setuptools  
RUN sudo apt-get -y install python-dev  
RUN sudo apt-get -y install build-essential  
RUN sudo apt-get -y install python-psycopg2  
RUN sudo apt-get -y install libpq-dev  
RUN sudo apt-get install -y libmysqlclient-dev  
RUN sudo apt-get install -y python-dev  
RUN sudo easy_install pip  
RUN sudo pip install --upgrade pip  
RUN sudo pip install MySQL-python  
RUN sudo pip install Flask  
RUN sudo pip install nose  
  
#Instalar la app  
RUN cd Proyecto-IV-modulo3 && sudo pip install -r requirements.txt  

