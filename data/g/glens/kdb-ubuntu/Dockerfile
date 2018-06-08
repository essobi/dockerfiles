# Dockerfile to run 32bit kdb+ on ubuntu  
# Created by douah  
FROM ubuntu:12.04  
MAINTAINER douah <github.com/douah>  
  
# Set Env variables for q  
ENV QHOME /q  
ENV PATH ${PATH}:${QHOME}/l32/  
  
# Install kdb+  
RUN \  
apt-get update && \  
apt-get install -y curl rlwrap unzip ia32-libs && \  
curl --silent -O kx.com/347_d0szre-fr8917_llrsT4Yle-5839sdX/3.2/linux.zip && \  
unzip linux.zip && \  
rm linux.zip && \  
alias q='rlwrap q'  
  
WORKDIR /  

