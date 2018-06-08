FROM debian:wheezy  
MAINTAINER Tilo Werner tilo.werner@moosbee.de  
  
ENV DEBIAN_FRONTEND=noninteractiv  
ENV DEB_RN=wheezy  
ENV SOGO_VERSION=3.2.0  
ENV SOGO_VERSION_ADDON=$DEB_RN-1  
ENV PKG_MAINTAINER="Tilo Werner <tilo.werner@moosbee.de>"  
ENV PKG_URGENCY=low  
ENV BUILD_DIR=/sogo-build  
ENV CHANGELOG_TEMPLATE=/tmp/changelog.template  
ENV DPKG_BUILDPACKAGE_OPTS="-F"  
VOLUME $BUILD_DIR  
  
RUN echo "APT::Get::Install-Recommends "false";" >>
/etc/apt/apt.conf.d/ZZ.conf  
RUN echo "APT::Get::Assume-Yes "true";" >> /etc/apt/apt.conf.d/ZZ.conf  
  
RUN apt-get update && apt-get install wget build-essential gnustep-make
libgnustep-base-dev gobjc libldap2-dev libpq-dev libmysqlclient-dev autotools-
dev debhelper libxml2-dev libsbjson-dev libsbjson2.3 libmemcached-dev
liblasso3-dev libcurl4-openssl-dev libexpat1-dev libpopt-dev libpopt0 vim &&
rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /entrypoint.sh  
COPY changelog.template /tmp/  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

