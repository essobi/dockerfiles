FROM evild/alpine-base:2.0.0  
MAINTAINER Dominique HAAS <contact@dominique-haas.fr>  
  
ARG ARIA2_VERSION=1.22.0  
  
RUN apk add \--no-cache \--virtual .build-deps build-base curl \  
&& apk add \--no-cache \--virtual .persistent-deps ca-certificates gnutls-dev
expat-dev sqlite-dev c-ares-dev \  
&& cd /tmp \  
&& curl -fSL
https://github.com/aria2/aria2/releases/download/release-${ARIA2_VERSION}/aria2-${ARIA2_VERSION}.tar.xz
-o aria2.tar.xz \  
&& tar xJf aria2.tar.xz \  
&& cd aria2-${ARIA2_VERSION} \  
&& ./configure \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& apk del .build-deps \  
&& rm -rf /tmp  
  
EXPOSE 6800  
  
ADD root /  

