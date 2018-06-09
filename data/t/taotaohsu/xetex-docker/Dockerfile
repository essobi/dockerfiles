FROM debian:jessie  
MAINTAINER Taotao Hsu <taotaohsu@gmail.com>  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install -y \  
texlive-xetex  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /var/texlive  
WORKDIR /var/texlive  

