FROM ubuntu:16.04  
LABEL maintainer="akshmakov@nc5ng.org"  
  
WORKDIR /workspace  
  
COPY install.sh /opt/gmt/install.sh  
  
## Do This in One Go to Minimize Docker Image Size  
ARG GSSHG_VERSION  
ARG DCW_VERSION  
ARG GMT_BRANCH  
ARG GMT_CMAKE_ARGS  
ENV GSSHG_VERSION=${GSSHG_VERSION:-2.3.7} DCW_VERSION=${DCW_VERSION:-1.1.3}
GMT_BRANCH=${GMT_BRANCH:-trunk} GMT_CMAKE_ARGS=${GMT_CMAKE_ARGS:-""}  
  
RUN apt-get update -y && \  
apt-get install -y \  
software-properties-common \  
python-software-properties && \  
add-apt-repository universe && \  
apt-get update && \  
apt-get install -y \  
subversion \  
build-essential \  
cmake \  
libcurl4-gnutls-dev \  
libnetcdf-dev \  
libgdal1-dev \  
libfftw3-dev \  
libpcre3-dev \  
liblapack-dev \  
libblas-dev \  
graphicsmagick \  
wget &&\  
(cd /opt/gmt && ./install.sh) && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/local/bin/gmt"]  

