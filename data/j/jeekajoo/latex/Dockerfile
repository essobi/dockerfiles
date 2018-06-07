FROM debian:jessie  
MAINTAINER Jeekajoo <github@fralef.me>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q  
RUN apt-get install -qy texlive-full  
RUN apt-get install -qy python-pygments  
RUN apt-get install -qy gnuplot  
  
WORKDIR /data  
VOLUME ["/data"]  

