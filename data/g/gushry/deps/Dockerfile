FROM debian:jessie  
  
#RUN apt-get update && rm -rf /var/lib/apt/lists/*  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
RUN apt-get update && apt-get install -y wget unzip  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LANG ja_JP.UTF-8  
RUN env  

