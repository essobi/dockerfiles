# Ubuntu Trusty Dockerfile  
FROM ubuntu:14.04.3  
MAINTAINER Rafał bluszcz Zawadzki <bluszcz@bluszcz.net>  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install qt5-default build-essential libsfml-dev -y  
RUN apt-get clean  
RUN echo 'debconf debconf/frontend select Dialog' | debconf-set-selections  

