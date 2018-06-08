# Godep + ffmpeg  
#  
# VERSION 1.0  
FROM oceanwu/godep:latest  
  
MAINTAINER oceanwu<wuhaiyang1213@gmail.com>  
  
# install FFMPEG  
RUN echo "deb http://www.deb-multimedia.org jessie main" >>
/etc/apt/sources.list  
  
RUN apt-get -y update  
  
RUN apt-get install -y --force-yes deb-multimedia-keyring  
  
RUN apt-get -y update  
  
RUN apt-get install -y ffmpeg  

