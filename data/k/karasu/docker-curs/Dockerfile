FROM library/debian:wheezy  
MAINTAINER Gustau Castells <gcastel9@ies-sabadell>  
RUN apt-get update && \  
apt-get -u upgrade && \  
apt-get install -y iputils-ping netcat-traditional && \  
apt-get clean && apt-get autoclean && \  
rm -rf /var/lib/apt/lists/*  
  

