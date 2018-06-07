ARG ALPINE_VERSION=latest  
FROM alpine:${ALPINE_VERSION}  
  
ENV DUMB_INIT_VERSION=1.2.1 GOSU_VERSION=1.10  
  
ADD rootfs /  
  
RUN set -x \  
&& apk add --no-cache --update curl \  
&& curl -SL https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 > /usr/bin/dumb-init \  
&& chmod +x /usr/bin/dumb-init \  
&& curl -SL
https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64 >
/usr/bin/gosu \  
&& chmod +x /usr/bin/gosu \  
&& chmod +x /usr/bin/createuser  

