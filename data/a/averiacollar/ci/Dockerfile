FROM alpine:3.7  
  
ENV GLIBC_VERSION='2.26-r0' \  
DOCKER_COMPOSE_VERSION='1.17.1'  
  
RUN apk add --no-cache \  
docker==17.12.1-r0 \  
git==2.15.0-r1 \  
openssh==7.5_p1-r8  
  
# install docker-compose  
RUN set -x && \  
apk add --no-cache -t .deps curl==7.59.0-r0 && \  
# Install glibc on Alpine (required by docker-compose) from  
# https://github.com/sgerrand/alpine-pkg-glibc  
# See also https://github.com/gliderlabs/docker-alpine/issues/11  
curl -Lso /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
curl -Lso glibc.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-$GLIBC_VERSION.apk && \  
curl -Lso glibc-bin.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-bin-$GLIBC_VERSION.apk && \  
apk add --no-cache glibc.apk glibc-bin.apk && \  
# Install docker-compose  
# https://docs.docker.com/compose/install/  
DOCKER_COMPOSE_URL=https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-`uname -s`-`uname -m` && \  
curl -Lso /usr/local/bin/docker-compose $DOCKER_COMPOSE_URL && \  
chmod a+rx /usr/local/bin/docker-compose && \  
# Basic check it works  
docker-compose version && \  
# Clean-up  
rm glibc.apk glibc-bin.apk && \  
apk del .deps  

