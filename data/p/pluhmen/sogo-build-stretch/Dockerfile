FROM debian:stretch  
MAINTAINER Tilo Werner tilo.werner@moosbee.de  
  
ENV DEBIAN_FRONTEND=noninteractiv  
ENV DEB_RN=stretch  
ENV SOGO_VERSION=3.2.10  
ENV SOGO_VERSION_ADDON=$DEB_RN-1  
ENV PKG_MAINTAINER="Tilo Werner <tilo.werner@moosbee.de>"  
ENV PKG_URGENCY=low  
ENV BUILD_DIR=/sogo-build  
ENV SOGO_CHANGELOG=/tmp/changelog.template  
  
VOLUME $BUILD_DIR  
  
RUN apt-get update && apt-get --yes --no-install-recommends install wget
build-essential gnustep-make libgnustep-base-dev gobjc libldap2-dev libpq-dev
libmariadbclient-dev libmariadbclient-dev-compat autotools-dev debhelper
libxml2-dev libsbjson-dev libsbjson2.3 libmemcached-dev liblasso3-dev
libcurl4-openssl-dev libexpat1-dev libpopt-dev libpopt0 python vim  
  
COPY entrypoint.sh /entrypoint.sh  
COPY changelog.template /tmp/  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

