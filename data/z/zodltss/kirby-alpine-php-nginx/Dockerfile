FROM nginx:alpine  
MAINTAINER Zac Duncan-Lee <zac@thesinkingship.com.au>  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade && \  
apk add php-fpm php-curl php-dom php-openssl php-xml php-json && \  
rm -rf /var/cache/apk/* && \  
mkdir /app  
  
VOLUME /app  
  
COPY ./default.conf /etc/nginx/conf.d/  
COPY ./code /app  
  
CMD nginx && php-fpm -F

