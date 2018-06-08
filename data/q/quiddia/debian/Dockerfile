FROM debian:latest  
MAINTAINER Radek Antoniuk <radek.antoniuk@quiddia.com>  
  
ENV packages bzip2 ca-certificates curl nano screen  
ENV opts "--yes --no-install-recommends --force-yes"  
RUN apt-get update && \  
apt-get install ${opts} ${packages} && \  
apt-get clean  
  
  

