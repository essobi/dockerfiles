FROM node:8-alpine  
  
ENV GLIBC 2.23-r3  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash curl git openssh-client  
  
RUN apk add --no-cache openssl ca-certificates && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC/glibc-$GLIBC.apk && \  
apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk && \  
ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \  
ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib  
  
ENV DOCKER_COMPOSE_VER 1.11.2  
  
RUN /bin/bash -c \  
set -x && \  
curl -L https://github.com/docker/compose/releases/download/1.11.2/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
ENV DOCKER_VER 17.03.0-ce  
  
RUN /bin/bash -c \  
set -x && \  
curl -L -o /tmp/docker-$DOCKER_VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VER.tgz && \  
tar -xz -C /tmp -f /tmp/docker-$DOCKER_VER.tgz && \  
mv /tmp/docker/* /usr/bin  

