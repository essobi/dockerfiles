FROM ubuntu:14.04  
MAINTAINER Yves Dubromelle "yves+git@dubronetwork.fr"  
ENV DEBIAN_FRONTEND noninteractive  
  
# System dependancies  
RUN apt-get update && \  
apt-get install -y \  
build-essential binutils-doc autoconf flex bison libjpeg-dev \  
libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses-dev \  
automake libtool libffi-dev curl git tmux gettext locales \  
python3 python3-pip python-dev python3-dev python-pip \  
libxml2-dev libxslt-dev libpq-dev  
  
# Taiga copy  
COPY taiga-back /taiga  
WORKDIR /taiga  
  
# Python dependancies  
RUN pip3 install -r requirements.txt  
  
# Custom files and scripts  
COPY db_init.sh /taiga/db_init.sh  
  
# Docker settings  
VOLUME ["/taiga/static","/taiga/media"]  
EXPOSE 8000  
# Default command  
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]  

