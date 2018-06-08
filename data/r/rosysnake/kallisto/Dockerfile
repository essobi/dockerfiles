FROM ubuntu:14.04  
  
ENV
SRC=https://github.com/pachterlab/kallisto/releases/download/v0.43.0/kallisto_linux-v0.43.0.tar.gz
ZIP=kallisto_linux-v0.43.0.tar.gz DST=/bin  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER root  
  
RUN apt-get -y update && apt-get -yy install wget && \  
cd $DST && \  
wget $SRC && \  
tar -xvf $ZIP && rm $ZIP && cp $DST/kallisto_linux-v0.43.0/kallisto .  
  
WORKDIR /data/  
  

