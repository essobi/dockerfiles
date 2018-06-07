FROM node:carbon-alpine  
  
MAINTAINER NoOne  
  
USER root  
  
RUN apk add --update build-base \  
&& rm -rf /root/src /tmp/* /usr/share/man /var/cache/apk/* \  
/root/.npm /root/.node-gyp /usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html \  
&& apk search --update  
  

