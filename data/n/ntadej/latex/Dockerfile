FROM blang/latex  
  
MAINTAINER Tadej Novak <tadej@tano.si>  
  
RUN apt-get -y update && \  
apt-get -yq install biber && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
VOLUME ["/data"]  

