FROM node  
MAINTAINER Adrian Gschwend <adrian.gschwend@zazuko.com>  
  
RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y -t jessie-backports openjdk-8-jre-headless  

