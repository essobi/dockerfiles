FROM ubuntu:12.04  
MAINTAINER shadowfaxchc "tim.messier@gmail.com"  
RUN apt-get update  
RUN apt-get install -y python-pip python-dev libxml2 libgeoip-dev libpq-dev
libmysqlclient-dev wget curl gcc mercurial git-core openjdk-6-jre-headless
libxslt1-dev libjpeg-dev language-pack-en libffi-dev  
RUN pip install tox  
RUN wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
-O /usr/share/GeoLiteCity.dat.gz  
RUN gunzip /usr/share/GeoLiteCity.dat  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

