FROM alpine:3.6 AS builder  
  
WORKDIR /src  
  
COPY . .  
  
RUN apk add --update-cache \  
nodejs \  
nodejs-npm \  
git \  
build-base \  
libtool \  
file \  
zlib  
  
RUN npm install  
  
RUN ./node_modules/.bin/gulp build --production  
  
FROM alpine:3.6  
RUN apk add --update-cache \  
nginx && \  
rm -rv /var/cache/apk/* && \  
rm -rf /var/www && \  
mkdir -p /run/nginx/  
  
COPY \--from=builder /src/dependency-deploy-config.txt /srv/  
COPY \--from=builder /src/dist /var/www/  
COPY \--from=builder /src/docker/default.conf /etc/nginx/conf.d/  
  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  
  
EXPOSE 80  
VOLUME /var/log/nginx  
  
# Volumes  
# - Conf: /etc/nginx/conf.d (default.conf)  
# - Cache: /var/cache/nginx  
# - Logs: /var/log/nginx  
# - Data: /var/www  

