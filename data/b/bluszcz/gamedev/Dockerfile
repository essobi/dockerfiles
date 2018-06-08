# Godot CI Dockerfile  
FROM bluszcz/godot-16.04  
MAINTAINER Rafał bluszcz Zawadzki <bluszcz@bluszcz.net>  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y -qq libsfml-dev build-essential games-c++-dev libcsfml-
dev git  
  
RUN apt-get clean  
  
RUN mkdir /opt/  
RUN cd /opt  
RUN git clone https://github.com/mxe/mxe.git  
RUN cd /opt/mxe  
RUN make sfml  
  
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections  

