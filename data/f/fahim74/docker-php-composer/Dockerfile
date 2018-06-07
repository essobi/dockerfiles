FROM php:7.1-alpine  
  
ARG NODE_VERSION=8.9.0  
LABEL php_version=7.1.10  
LABEL node_version=$NODE_VERSION  
  
RUN apk add --no-cache \  
bash coreutils tar \  
make gcc g++ python \  
linux-headers binutils-gold readline readline-dev \  
gnupg nasm libstdc++ git \  
alpine-sdk autoconf build-base zlib \  
zlib-dev libpng libpng-dev libwebp \  
libwebp-dev libjpeg-turbo libjpeg-turbo-dev  
  
RUN cd /tmp \  
&& curl https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.gz
> nodejs-src.tar.gz \  
&& tar xf nodejs-src.tar.gz \  
&& cd node-v${NODE_VERSION} \  
&& ./configure --prefix=/usr \  
&& make -j`getconf _NPROCESSORS_ONLN` \  
&& make install  
RUN rm -rf /tmp/*  
  
# Yarn  
RUN npm install -g yarn  
  
MAINTAINER Fahim Shariar <fahim.shoumik@gmail.com>  
  
RUN apk add --no-cache \  
ca-certificates  
  
# set up nsswitch.conf for Go's "netgo" implementation (which Docker
explicitly uses)  
# - https://github.com/docker/docker-
ce/blob/v17.09.0-ce/components/engine/hack/make.sh#L149  
# - https://github.com/golang/go/blob/go1.9.1/src/net/conf.go#L194-L275  
# - docker run --rm debian:stretch grep '^hosts:' /etc/nsswitch.conf  
RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' >
/etc/nsswitch.conf  
  
ENV DOCKER_CHANNEL test  
ENV DOCKER_VERSION 17.10.0-ce-rc2  
# TODO ENV DOCKER_SHA256  
# https://github.com/docker/docker-
ce/blob/5b073ee2cf564edee5adca05eee574142f7627bb/components/packaging/static/hash_files
!!  
# (no SHA file artifacts on download.docker.com yet as of 2017-06-07 though)  
RUN set -ex; \  
# why we use "curl" instead of "wget":  
# + wget -O docker.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-17.03.1-ce.tgz  
# Connecting to download.docker.com (54.230.87.253:443)  
# wget: error getting response: Connection reset by peer  
apk add \--no-cache --virtual .fetch-deps \  
curl \  
tar \  
; \  
\  
# this "case" statement is generated via "update.sh"  
apkArch="$(apk --print-arch)"; \  
case "$apkArch" in \  
x86_64) dockerArch='x86_64' ;; \  
aarch64) dockerArch='aarch64' ;; \  
ppc64le) dockerArch='ppc64le' ;; \  
s390x) dockerArch='s390x' ;; \  
*) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\  
esac; \  
\  
if ! curl -fL -o docker.tgz
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz";
then \  
echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from
'${DOCKER_CHANNEL}' for '${dockerArch}'"; \  
exit 1; \  
fi; \  
\  
tar --extract \  
\--file docker.tgz \  
\--strip-components 1 \  
\--directory /usr/local/bin/ \  
; \  
rm docker.tgz; \  
\  
apk del .fetch-deps; \  
\  
dockerd -v; \  
docker -v  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  

