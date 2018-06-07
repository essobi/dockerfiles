FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
ca-certificates \  
build-essential \  
cmake \  
qt5-default \  
python \  
liblog4cpp5-dev \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

