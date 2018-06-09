FROM debian:jessie-slim  
MAINTAINER Javier Fernández-Bravo Peñuela <fraferp9@posgrado.upv.es>  
LABEL description="Docker image of Debian + NodeJS and ZeroMQ"  
  
RUN echo "deb http://ftp.es.debian.org/debian/ testing main contrib non-free"
>> /etc/apt/sources.list  
RUN echo "deb-src http://ftp.es.debian.org/debian/ testing main contrib non-
free" >> /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
debconf-utils dialog  
RUN apt-get install -y --no-install-recommends wget build-essential python
gnutls-bin aptitude vim libtool pkg-config autoconf automake uuid-dev
libsodium-dev gcc libc6-dev make ca-certificates  
RUN apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/*  
  
ENV NODEJS_VERSION 8.9.3  
ENV ZEROMQ_VERSION 4.1.6  
WORKDIR /tmp  
RUN wget
https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}.tar.gz  
RUN tar -xvzf node-v${NODEJS_VERSION}.tar.gz  
WORKDIR /tmp/node-v${NODEJS_VERSION}  
RUN ./configure  
RUN make -j `nproc`  
RUN make install  
  
WORKDIR /tmp  
RUN wget
https://github.com/zeromq/zeromq4-1/releases/download/v${ZEROMQ_VERSION}/zeromq-${ZEROMQ_VERSION}.tar.gz  
RUN tar -xvzf zeromq-${ZEROMQ_VERSION}.tar.gz  
WORKDIR /tmp/zeromq-${ZEROMQ_VERSION}  
RUN ./configure  
RUN make -j `nproc`  
RUN make install  
RUN ldconfig  
  
WORKDIR /tmp  
RUN rm -Rf node-v${NODEJS_VERSION}.tar.gz node-v${NODEJS_VERSION}  
RUN rm -Rf zeromq-${ZEROMQ_VERSION}.tar.gz zeromq-${ZEROMQ_VERSION}  
  
WORKDIR /  
  

