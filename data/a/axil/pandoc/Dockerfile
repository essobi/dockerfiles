FROM ubuntu:16.04  
  
MAINTAINER Achilleas Pipinellis <axilleas@axilleas.me>  
  
RUN apt-get update && apt-get install -y wget git ruby  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN wget -O pandoc.deb
https://github.com/jgm/pandoc/releases/download/1.17.0.2/pandoc-1.17.0.2-1-amd64.deb  
  
RUN dpkg -i pandoc.deb  

