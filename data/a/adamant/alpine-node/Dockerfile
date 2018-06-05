FROM alpine:3.5  
MAINTAINER Adam Dodman <adam.dodman@gmx.com>  
  
RUN apk add --no-cache nodejs  
  
RUN find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf && \  
rm -rf /usr/share/man /tmp/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
ENTRYPOINT ["node"]  
  

