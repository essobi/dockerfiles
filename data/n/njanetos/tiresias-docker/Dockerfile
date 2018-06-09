FROM debian:latest  
MAINTAINER njanetos <nejanetos@gmail.com>  
LABEL Description="Build environment for the tiresias engine"  
  
RUN rm -rf /var/lib/apt/lists/* && \  
echo 'deb http://ftp.debian.org/debian/ stretch main' >> /etc/apt/sources.list
&& \  
apt-get update && \  
apt-get install -y g++-6 libboost-all-dev git make libarmadillo-dev libnlopt-
dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

