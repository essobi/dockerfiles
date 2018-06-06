FROM ubuntu:17.10  
  
MAINTAINER Daniel Rippen <rippendaniel@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TZ=Europe/Berlin  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
&& \  
export LANG=C.UTF-8 && \  
apt-get update && \  
apt-get -y install apt-utils && \  
apt-get -y upgrade  && \  
apt-get install -y software-properties-common python-software-properties && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

