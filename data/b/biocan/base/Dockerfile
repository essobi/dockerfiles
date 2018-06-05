######  
# Dockerfile  
# Version : 1.0.0  
# maintainer: Natapol  
# base image: alpine:3.3  
#  
# build command: docker build --rm -t biocan/base:1.0.0 -t biocan/base:latest
.  
######  
FROM alpine:3.3  
# installing from alpine  
RUN apk add --update curl \  
gcc \  
libc-dev \  
zlib-dev \  
ncurses-dev \  
make  
  
# install external software  
# working environment  
RUN mkdir /bcdata  
VOLUME ["/bcdata"]  
CMD ["/bin/sh"]  
WORKDIR /bcdata  
  
# Maintainer  
MAINTAINER Natapol Pornputtapong <natapol.por@gmail.com>  
  
# short description  
# minimal docker container for bioinformatics software: base  

