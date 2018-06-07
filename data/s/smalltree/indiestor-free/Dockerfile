FROM ubuntu:14.04  
MAINTAINER Keri Alleyne <info@symlogix.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
RUN apt-get update && apt-get install -y \  
nano \  
wget  
RUN wget -q -O - http://free.indiestor.com/indiestor-free.key | apt-key add -  
RUN echo "deb http://free.indiestor.com/apt/ubuntu trusty main" | tee -a
/etc/apt/sources.list.d/indiestor-free.list  
RUN apt-get update && apt-get install -y -o Dpkg::Options::="--force-confnew"
\  
indiestor-free-gui  
RUN useradd -ms /bin/bash admin  
RUN usermod -a -G indiewheel admin  
COPY startup.sh /root/  

