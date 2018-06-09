FROM debian:stable-slim  
  
RUN apt-get update && apt-get install -y \  
libssl-dev \  
libjansson-dev \  
libcurl4-openssl-dev \  
build-essential \  
autoconf \  
automake  
  
ADD . /data  
  
WORKDIR /data  
  
RUN LDFLAGS='-lcurl -ljansson' ./configure && make install  
  
CMD stunnel /data/stunnel.conf  

