FROM alpine:latest  
  
# Based on https://github.com/monostream/docker-rancher-
compose/blob/master/Dockerfile  
  
MAINTAINER Andrzej Ressel <andrzej.ressel@identt.pl>  
  
ARG RANCHER_COMPOSE_VERSION=0.12.4  
  
RUN apk add \--quiet --no-cache ca-certificates curl unzip && \  
curl -sSL "https://github.com/rancher/rancher-
compose/releases/download/v${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-
amd64-v${RANCHER_COMPOSE_VERSION}.tar.gz" | tar -xzp -C /usr/local/bin/
\--strip-components=2 && \  
rm -rf /var/cache/*  

