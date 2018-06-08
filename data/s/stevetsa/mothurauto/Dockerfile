# This is a comment  
FROM ubuntu:latest  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>  
RUN apt-get clean && apt-get update  
  
RUN apt-get install --yes \  
g++ \  
build-essential \  
gcc-multilib \  
apt-utils \  
wget \  
unzip  
  
# Get latest source from releases  
RUN wget
https://github.com/mothur/mothur/releases/download/v1.38.1/Mothur.linux_64.zip
&& \  
unzip Mothur.linux_64.zip && \  
rm Mothur.linux_64.zip  
  
#adds to the path  
ENV PATH /mothur:$PATH  
ENV TERM dumb  
  

