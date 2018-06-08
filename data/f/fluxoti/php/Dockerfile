FROM ambientum/php:7.2-nginx  
LABEL maintainer="mauri.nunes@fluxoti.com"  
  
ENV TERM=screen-256color  
  
USER root  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN apk add -u nodejs yarn nodejs-npm  
  
RUN apk add php7-pdo_sqlite@php php7-sockets@php  
  
RUN sed -i -e "s/memory_limit = 128M/memory_limit = 512M/g" /etc/php7/php.ini  
  
USER ambientum  
  
CMD ["/home/ambientum/start.sh"]

