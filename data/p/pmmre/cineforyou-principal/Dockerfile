FROM ubuntu:14.04  
  
#Autor  
MAINTAINER Pablo Martin-Moreno Ruiz <pmmr1990@gmail.com>  
  
#Actualizar Sistema Base  
RUN sudo apt-get -y update && sudo apt-get install -y python-setuptools
python-dev build-essential python-psycopg2 libpq-dev && sudo easy_install pip
&& sudo pip install --upgrade pip && sudo pip install Django  

