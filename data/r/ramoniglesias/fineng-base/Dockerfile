#Basic Image  
FROM ubuntu:14.04  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update  
#RUN apt-get install -y --force-yes git  
RUN apt-get install -y --force-yes nginx  
RUN apt-get install -y --force-yes build-essential  
RUN apt-get install -y --force-yes python-pip  
RUN pip install virtualenv  
RUN apt-get install -y --force-yes libblas-dev liblapack-dev gfortran
libfreetype6-dev libpng-dev python-dev libxft-dev libpq-dev  
  
#Create the folder where app lives  
#Assumes the entirety of my app is there  
RUN mkdir /var/www  
RUN mkdir /var/www/fineng-base  
RUN pip install numpy==1.9.1  
ADD ./requirements.txt /var/www/fineng-base/requirements.txt  
RUN pip install -r /var/www/fineng-base/requirements.txt  
  
#install Supervisor  
RUN apt-get install -y --force-yes supervisor  
  
  
#Set nginx and uwsgi configs  
RUN rm /etc/nginx/sites-enabled/default  
RUN mkdir -p /var/log/uwsgi  
RUN mkdir /etc/uwsgi  
RUN mkdir /etc/uwsgi/vassals  

