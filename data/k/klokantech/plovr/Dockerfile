FROM debian:8  
  
ENV DEBIAN_FRONTEND=noninteractive \  
PLOVR_DIR=/usr/local/bin \  
PLOVR=/usr/local/bin/plovr.jar \  
PLOVR_VERSION=6.1.1  
  
RUN apt-get -qq update \  
&& apt-get -qq -y --no-install-recommends install \  
openjdk-7-jre \  
make \  
rsync \  
wget \  
&& apt-get clean \  
&& mkdir -p $PLOVR_DIR \  
&& wget --no-check-certificate -q -P $PLOVR_DIR \  
https://github.com/bolinfest/plovr/releases/download/v$PLOVR_VERSION/plovr.jar  
  
EXPOSE 9810  
  
WORKDIR /data  

