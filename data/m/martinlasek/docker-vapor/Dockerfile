FROM ubuntu:16.04  
LABEL maintainer="martinlasek"  
  
RUN apt-get update && \  
apt-get install -y wget && \  
/bin/bash -c "$(wget -qO- https://apt.vapor.sh)" && \  
apt-get install -y \  
swift \  
vapor \  
libpython2.7 && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /vapor  

