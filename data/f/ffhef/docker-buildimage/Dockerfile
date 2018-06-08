FROM debian:stretch-slim  
  
MAINTAINER cbk@freifunk-hennef.de  
  
RUN apt-get update -y && apt-get dist-upgrade -y && \  
apt-get install -y ecdsautils git subversion python build-essential gawk unzip
libncurses5-dev zlib1g-dev libssl-dev wget cmake pkg-config curl ca-
certificates && \  
apt-get clean && rm -rf /var/lib/apt/lists /tmp/* /var/tmp/*  

