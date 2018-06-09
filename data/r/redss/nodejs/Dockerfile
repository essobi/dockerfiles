FROM debian:jessie  
MAINTAINER Andrea Chiumenti <achiumenti@red.software.systems>  
  
LABEL description node image with full intl support  
  
ENV NODE_VERSION="v7.4.0"  
RUN apt-get update -q && \  
apt-get install -qy \  
curl \  
build-essential \  
libtool-bin \  
autoconf \  
pkg-config \  
python \  
git \  
locales \  
libicu-dev  
  
# Download specific version of zeromq and install  
WORKDIR /tmp  
  
RUN curl -LO
https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz && \  
tar -xzf node-${NODE_VERSION}.tar.gz  
  
RUN cd node-${NODE_VERSION} && \  
./configure --with-intl=full-icu --download=all && \  
make && make install  
  
# Cleanup  
RUN rm /tmp/* -rf  
  
WORKDIR /app  
VOLUME ["/app"]  
  
CMD ["node", "."]  

