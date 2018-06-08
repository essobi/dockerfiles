# Set base image.  
FROM alpine:latest  
  
MAINTAINER Dominik Hahn <dominik@monostream.com>  
  
# Define rancher-compose version  
ENV RANCHER_COMPOSE_VERSION=v0.8.6  
  
# Install dependencies and rancher-compose  
RUN apk add --quiet --no-cache ca-certificates && \  
apk add --quiet --no-cache --virtual build-dependencies curl && \  
curl -sSL "https://github.com/rancher/rancher-
compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-
amd64-${RANCHER_COMPOSE_VERSION}.tar.gz" | tar -xz -C /usr/local/bin/
\--strip-components=2 && \  
chmod +x /usr/local/bin/rancher-compose && \  
apk del build-dependencies && \  
rm -rf /var/cache/*  
  
# Set working directory  
WORKDIR /workspace  
  
# Executing defaults  
CMD ["/bin/sh"]

