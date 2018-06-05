FROM ubuntu:xenial  
  
LABEL version="1.0"  
  
MAINTAINER Marc Peña Segarra <segarrra@gmail.com>  
  
# Tell debconf to run in non-interactive mode (but just during the image
build).  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get dist-upgrade -yf && \  
apt-get install -y \  
git vim make automake gcc g++ cmake python && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# This seems to be the most up to date fork  
RUN git clone \--depth 1 https://github.com/joswr1ght/kraken && \  
cd kraken && \  
make noati  
  
#WORKDIR /kraken/Kraken  
ENTRYPOINT ["/bin/bash"]  

