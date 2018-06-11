FROM alpine:3.4  
MAINTAINER andy@betacode.io  
  
ENV PACKAGES="build-base wget git libtool pkgconfig autoconf automake"  
# Install prerequisites to compile the libraries  
RUN apk --update --upgrade add $PACKAGES && \  
find / -type f -iname \\*.apk-new -delete && \  
rm -rf /var/cache/apk/*  
  
# Download specific version of zeromq and install  
RUN cd /tmp && \  
wget
https://github.com/zeromq/libzmq/releases/download/v${ZEROMQ_VERSION:-4.2.0}/zeromq-${ZEROMQ_VERSION:-4.2.0}.tar.gz
&& \  
tar -xzf zeromq-${ZEROMQ_VERSION:-4.2.0}.tar.gz && cd
zeromq-${ZEROMQ_VERSION:-4.2.0} && \  
./autogen.sh && ./configure && make && make install  
  
# Cleanup  
RUN rm /tmp/zeromq-${ZEROMQ_VERSION:-4.2.0}* -rf && rm /tmp/* -rf  

