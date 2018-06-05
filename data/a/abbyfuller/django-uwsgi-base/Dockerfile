FROM ubuntu:trusty  
  
MAINTAINER Abby Fuller <abby.fuller@gmail.com>  
  
RUN apt-get install -y software-properties-common && add-apt-repository -y
ppa:nginx/stable && apt-get update && apt-get -y install git \  
mercurial \  
libjpeg-dev \  
python \  
python-dev \  
python-setuptools \  
python-software-properties \  
supervisor \  
libpq-dev \  
libxml2-dev \  
libxslt1-dev \  
nginx \  
libgeos-dev  
  
RUN apt-get clean autoclean && apt-get autoremove && rm -rf
/var/lib/{apt,dpkg,cache,log}/  
  
RUN easy_install pip && pip install uwsgi  

