FROM haffmans/cmake-qt5:latest  
MAINTAINER Wouter Haffmans <wouter@simply-life.net>  
  
WORKDIR /  
RUN wget "https://git.simply-life.net/packages/ubuntu/xenial/qommando-
master.tar.bz2" -O /tmp/qommando-master.tar.bz2 \  
&& tar -jxvf /tmp/qommando-master.tar.bz2 \  
&& rm /tmp/qommando-master.tar.bz2  
  
# Use devel for this image...  
USER devel  
ENV HOME=/home/devel  
WORKDIR /home/devel  
  
# ... but revert to root on the next image builds  
ONBUILD USER root  
ONBUILD WORKDIR /  

