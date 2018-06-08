FROM ubuntu:14.04  
MAINTAINER Jonathan Stoppani "jonathan@stoppani.name"  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN /usr/sbin/locale-gen en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN /usr/bin/apt-get update && /usr/bin/apt-get -y upgrade  
  
RUN /usr/bin/apt-get install -y \  
python-dev python-pip \  
libxml2-dev libxslt1-dev \  
postgresql-client-9.3 libpq5 \  
libpq-dev \  
libjpeg-dev libjpeg8-dev \  
libfreetype6-dev \  
zlib1g-dev libpng12-dev \  
libtiff4-dev \  
liblcms2-dev libwebp-dev \  
tcl8.6-dev tk8.6-dev python-tk \  
libmysqlclient-dev \  
git  

