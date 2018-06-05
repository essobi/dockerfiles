FROM debian:jessie  
MAINTAINER Subak Systems <info@subak.jp>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
build-essential \  
libncurses5-dev \  
libgsm1-dev \  
libjansson-dev \  
libogg-dev \  
libsqlite3-dev \  
libsrtp0-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
uuid \  
uuid-dev \  
libpopt-dev \  
libspandsp-dev \  
libvorbis-dev \  
curl \  
ca-certificates \  
openssl \  
unixODBC \  
unixODBC-dev \  
libmyodbc \  
speex \  
libspeex-dev \  
libspeexdsp-dev  
  
ARG ASTERISK_VERSION=13.13.1  
ENV PKG_NAME ${ASTERISK_VERSION}  
  
WORKDIR /usr/src  
RUN curl -L -o /usr/src/${PKG_NAME}.tar.gz
https://github.com/asterisk/asterisk/archive/${ASTERISK_VERSION}.tar.gz \  
&& tar zxfv ${PKG_NAME}.tar.gz  
  
RUN cd asterisk-*/pbx/.. \  
&& ./configure \  
&& make bininstall  
  
RUN apt-get clean  
  
WORKDIR /etc/asterisk  
CMD ["asterisk","-f"]  

