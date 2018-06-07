FROM debian:jessie  
MAINTAINER Alexis Horgix Chotard <alexis.horgix.chotard@gmail.com>  
  
RUN apt-get update && apt-get install -y texlive-full  
  
RUN mkdir /var/sources  
  
WORKDIR /var/sources  
  
CMD xelatex  

