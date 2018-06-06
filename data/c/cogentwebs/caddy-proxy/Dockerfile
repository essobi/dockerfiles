FROM cogentwebs/caddy  
MAINTAINER Pichate Ins <cogent@cogentwebworks.com>  
  
# Set labels  
LABEL com.caddy-proxy.cogentwebworks.version="0.1.1-beta"  
  
# ROOTFS  
COPY rootfs /  
  
ARG FOREGO_VERSION="0.16.1"  
ARG DOCKER_GEN_VERSION="0.7.4"  
ENV CADDYPATH="usr/local/etc/caddy/"  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
# Install wget and install/updates certificates  
RUN apk-install openssh-client git && \  
apk add --no-cache --virtual .build-dependencies curl wget tar && \  
wget --quiet "https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-alpine-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz" && \  
tar -C /usr/bin -xvzf "docker-gen-alpine-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz" && \  
rm "/docker-gen-alpine-linux-amd64-$DOCKER_GEN_VERSION.tar.gz" && \  
apk-clean  
  
# ensure www-data user exists  
# Add the files  
ADD rootfs /  
  
# Expose the ports for caddy  
EXPOSE 80 443 2015  
#VOLUME  
VOLUME ["/usr/html"]  
# INIT S6  
ENTRYPOINT [ "/init" ]

