FROM ubuntu:14.04  
MAINTAINER Alexander Skjolden alex@plastboks.net  
  
RUN apt-get update  
#RUN apt-get upgrade  
RUN apt-get -y install build-essential git  
  
VOLUME /byol/shared  
  
WORKDIR /byol  
RUN git clone https://github.com/plastboks/Byol.git app  
WORKDIR /byol/app  
RUN make  

