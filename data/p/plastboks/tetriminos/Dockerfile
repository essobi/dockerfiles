FROM ubuntu:14.04  
MAINTAINER Alexander Skjolde alex@plastboks.net  
  
RUN apt-get update  
#RUN apt-get upgrade  
RUN apt-get -y install build-essential  
RUN apt-get -y install git  
RUN apt-get -y install libreadline-dev libedit-dev  
RUN apt-get -y install libncurses5-dev  
  
VOLUME /tetriminos/shared  
  
WORKDIR /tetriminos  
RUN git clone https://github.com/plastboks/Tetriminos.git app  
WORKDIR /tetriminos/app  
RUN make  

