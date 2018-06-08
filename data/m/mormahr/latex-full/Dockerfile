FROM debian:jessie  
MAINTAINER Moritz Mahringer <me@moritzmahringer.de>  
  
RUN apt-get update && \  
apt-get install -y texlive-full rubber && \  
apt-get autoclean && apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir /data  
  
WORKDIR /data  

