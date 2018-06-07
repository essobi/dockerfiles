FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y \--quiet upgrade && \  
apt-get -y \--quiet install libxml2-dev libxslt1-dev git python python-
setuptools python-dev build-essential libz-dev lsb openssl dnsutils curl rsync
iptraf-ng rdiff ethtool iotop libtool pv curl unzip zip inotify-tools && \  
apt-get -y \--quiet install python-software-properties software-properties-
common htop pwgen npm nodejs-legacy nodejs gcc libc6-dev make wget vim nano &&
\  
easy_install pip && \  
pip \--no-input install envtpl && \  
apt-get -y update && \  
apt-get -y clean && \  
npm install -g wait-for-mongo && \  
npm install -g http-server  
  
# GO FROM OFFICIAL REPO : https://registry.hub.docker.com/_/golang/  
  
ENV GOLANG_VERSION 1.4.2  
  
RUN curl -sSL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz | tar -v -C
/usr/src -xz && \  
cd /usr/src/go/src && ./make.bash \--no-clean 2>&1 && \  
mkdir -p /go/src /go/bin && chmod -R 777 /go  
  
ENV PATH /usr/src/go/bin:$PATH  
ENV GOPATH /go  
ENV PATH /go/bin:$PATH  

