FROM ubuntu:latest  
  
MAINTAINER Bogdan Alin Muresan <alinugr@gmail.com>  
  
RUN apt-get update  
  
#Download the app  
RUN apt-get install -y git  
RUN git clone https://github.com/bogdananas/proyectoIV-modulo2.git  
  
#instalar dependencias  
RUN apt-get install -y python-setuptools  
RUN apt-get -y install python-dev  
RUN apt-get -y install build-essential  
RUN apt-get -y install python-psycopg2  
RUN apt-get -y install libpq-dev  
RUN easy_install pip  
RUN pip install --upgrade pip  
RUN apt-get install -y net-tools  
  
EXPOSE 5000  
#instalamos la aplicaión  
RUN pwd  
RUN cd proyectoIV-modulo2 / && ls -l  
RUN pwd  
RUN cd proyectoIV-modulo2 && pip install -r requirements.txt --allow-all-
external

