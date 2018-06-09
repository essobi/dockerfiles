FROM ubuntu:latest  
MAINTAINER Michael Squires <sqmk@php.net>  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install stunnel4 -y  
  
COPY stunnel.conf /etc/stunnel  
  
WORKDIR /etc/stunnel  
  
ENTRYPOINT ["/usr/bin/stunnel"]  

