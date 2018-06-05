FROM nginx:stable-alpine  
  
MAINTAINER SmartThings Developers "developers@smartthings.com"  
ENV CONFD_VERSION "0.11.0"  
RUN \  
set -ex \  
&& apk add --no-cache --virtual .build-deps \  
curl \  
&& mkdir -p /usr/local/sbin \  
&& mkdir -p /opt/etc/nginx/sites-enabled \  
&& curl -fSL
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 -o /usr/local/sbin/confd \  
&& chmod 755 /usr/local/sbin/confd \  
&& apk del .build-deps  
  
EXPOSE 80 443  

