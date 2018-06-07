FROM alpine:3.5  
  
MAINTAINER Pedro Maia <pedro.maia@ezdelivery.co>  
  
RUN apk -U upgrade && \  
apk add --no-cache --update \  
curl \  
unzip \  
tar \  
gzip \  
ca-certificates && \  
update-ca-certificates --fresh && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
RUN curl -L \  
https://github.com/rancher/rancher-compose/releases/download/v0.12.5/rancher-
compose-linux-amd64-v0.12.5.tar.gz \  
-o rancher-compose.tar.gz && \  
tar zxvf rancher-compose.tar.gz --strip-components 2 && \  
rm -rf rancher-compose.tar.gz && \  
mv rancher-compose /usr/bin/rancher-compose && \  
chmod +x /usr/bin/rancher-compose  

