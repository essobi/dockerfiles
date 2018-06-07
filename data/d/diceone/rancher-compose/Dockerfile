FROM alpine:3.4  
MAINTAINER Dr. Doom <doom@dev-ops.de>  
  
# Define rancher compose version  
ENV RANCHER_COMPOSE_VERSION v0.8.6  
# Download and install rancher compose  
RUN apk add --no-cache --virtual .persistent-deps \  
ca-certificates \  
wget \  
tar \  
xz \  
&& wget -O /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz
"https://github.com/rancher/rancher-
compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-
amd64-${RANCHER_COMPOSE_VERSION}.tar.gz" \  
&& tar -xf /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz
-C /tmp \  
&& mv /tmp/rancher-compose-${RANCHER_COMPOSE_VERSION}/rancher-compose
/usr/local/bin/rancher-compose \  
&& rm -R /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz
/tmp/rancher-compose-${RANCHER_COMPOSE_VERSION}\  
&& chmod +x /usr/local/bin/rancher-compose  
  
CMD ["rancher-compose"]  

