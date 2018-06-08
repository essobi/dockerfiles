# Loaders  
# Image Loader  
# Markup Loader  
# References:  
#
http://docs.opencv.org/3.0-beta/doc/tutorials/introduction/desktop_java/java_dev_intro.html  
# http://rodrigoberriel.com/2014/10/installing-opencv-3-0-0-on-ubuntu-14-04/  
FROM node:latest  
MAINTAINER Ganesh Iyer "lastlegion@gmail.com"  
### update  
RUN apt-get -q update  
# RUN apt-get -q -y upgrade  
# RUN apt-get -q -y dist-upgrade  
# RUN apt-get install -q -y libcurl3  
### need build tools for building openslide and later iipsrv  
RUN apt-get -q -y install libcurl3 git  
  
RUN mkdir /root/src  
  
### prereqs for openslide  
RUN apt-get -q -y install zlib1g-dev libpng12-dev libjpeg-dev \  
libtiff5-dev libgdk-pixbuf2.0-dev libxml2-dev \  
libsqlite3-dev libcairo2-dev libglib2.0-dev  
  
WORKDIR /root/src  
  
# Openslide  
RUN apt-get install -y openslide-tools python3-openslide \  
python3 python3-setuptools python3-pip \  
nodejs npm  
  
# Data Loader API  
RUN mkdir -p /root/dataloader  
WORKDIR /root/dataloader  
EXPOSE 3002  
RUN git clone \--recursive https://github.com/camicroscope/ImageLoader.git .  
RUN git submodule update --recursive --remote  
RUN npm install  
  
RUN ["pip3","install", "-r", "/root/dataloader/DataLoader/requirements.txt"]  
  
# Install forever  
RUN ln -s "$(which nodejs)" /usr/bin/node  
RUN npm install -g forever  
COPY run.sh /root/run.sh  
RUN apt-get install -y default-jre  
COPY trusted-app-client-0.0.1-jar-with-dependencies.jar /root/  
COPY createUser.py /root/  
WORKDIR /root/  
CMD ["sh", "run.sh"]  

