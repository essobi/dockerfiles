FROM ubuntu:14.04  
MAINTAINER Joanna Ohradka <ohradka.joanna@gmail.com>  
RUN apt-get update  
RUN apt-get install -y build-essential  
RUN apt-get install -y cmake  
RUN apt-get install -y qt5-default  
RUN apt-get install -y libqt4-network  
RUN apt-get install -y openssl  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y x11-apps  
RUN apt-get install -y wget  
RUN apt-get install -y xmlstarlet  
  
ADD / /rso  
WORKDIR /rso  
  
ENV DISPLAY :0  

