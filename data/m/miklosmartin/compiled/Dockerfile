FROM buildpack-deps:wheezy-curl  
  
MAINTAINER Martin Miklós <miklos.martin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y libc6-dev gcc xdg-utils  
  
RUN wget http://downloads.dlang.org/releases/2014/dmd_2.066.1-0_amd64.deb -O
dmd.deb && \  
dpkg -i dmd.deb && \  
rm dmd.deb  
  
WORKDIR /app  
  
ENTRYPOINT ["dmd"]  

