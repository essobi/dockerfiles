FROM ubuntu:14.04  
  
MAINTAINER AttractGroup  
  
RUN apt-get update --fix-missing  
# Install build tools  
RUN apt-get install -y \  
git \  
build-essential \  
postgresql-server-dev-all \  
libxml2-dev \  
libxslt1-dev \  
libevent-dev \  
libffi-dev  
  
#Install pillow dependency  
RUN apt-get install -y \  
libtiff4-dev \  
libjpeg8-dev \  
zlib1g-dev \  
libfreetype6-dev \  
liblcms2-dev \  
libwebp-dev \  
tcl8.5-dev \  
tk8.5-dev \  
python-tk  
  
# Install python package  
RUN apt-get install -y \  
python \  
python-dev \  
python-setuptools \  
python-pip  
  
# Install postgres requirements  
RUN apt-get install -y \  
libgeos-dev \  
postgresql-client  
  
# Install redis  
#RUN apt-get install -y \  
# redis-server  
  
#RUN apt-get install -y npm  
#  
## Install bower  
#RUN apt-get install -y curl  
#RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
#RUN apt-get install -y nodejs  
#RUN npm install -g bower  
  
# Install ElasticSearch  
#RUN apt-get install -y \  
# openjdk-7-jre-headless \  
# wget  
#  
#RUN wget
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.4.deb  
#RUN dpkg -i elasticsearch-1.7.4.deb  
#RUN service elasticsearch start  
  
# Install supervisor  
#RUN apt-get install -y supervisor  
  
# update pip  
RUN pip install -U pip setuptools  
  
# Install nginx  
#RUN apt-get install -y nginx  
#RUN mkdir /etc/nginx/sites-enabled/  
#RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.default  
#RUN ln -s /home/docker/code/docker/conf/nginx.conf /etc/nginx/  
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf # set daemon off, because
supervisor can't work with nginx in daemon mode  
#RUN rm /etc/nginx/sites-enabled/default  
  
# Install uwsgi  
#RUN pip install uwsgi  
#RUN mkdir /var/log/uwsgi/  
  
# Create various dirs  
RUN mkdir /var/log/expertmatch/  
  
# Install requirements  
COPY ./req.txt /requirements/req.txt  
RUN pip install -r /requirements/req.txt  
  
#CMD ["/home/docker/code/docker/start.sh"]  

