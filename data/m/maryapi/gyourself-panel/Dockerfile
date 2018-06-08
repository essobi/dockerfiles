FROM mhart/alpine-node:6.9.1  
MAINTAINER Mert Dogar <mertdogar@gmail.com>  
  
WORKDIR /app  
ADD . .  
  
RUN apk update && \  
apk add --update nginx && \  
mkdir -p /tmp/nginx/client-body && \  
apk add --no-cache git && \  
npm install --unsafe-perm && \  
apk del git && \  
rm -rf /etc/ssl /root/.cache \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY config/nginx/panel.conf /etc/nginx/conf.d/panel.conf  
  
CMD ["/bin/sh", "scripts/startcontainer.sh"]  

