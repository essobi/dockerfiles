FROM docker:git  
MAINTAINER wTayyeb <wtayyeb@gmail.com>  
  
ARG RANCHER_COMPOSE_VERSION=v0.12.5  
  
RUN apk add \--no-cache \--virtual .fetch-deps wget tar \  
&& wget -qO- https://github.com/rancher/rancher-
compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-
amd64-${RANCHER_COMPOSE_VERSION}.tar.gz \  
| tar xz \--strip=1 ./rancher-compose-${RANCHER_COMPOSE_VERSION}/rancher-
compose -O > /usr/local/bin/rancher-compose \  
&& chmod +x /usr/local/bin/rancher-compose \  
&& apk del .fetch-deps \  
&& rancher-compose -v  

