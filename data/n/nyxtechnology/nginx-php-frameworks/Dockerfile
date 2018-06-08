ARG NGINX_VER=1.13  
  
FROM wodby/nginx:1.13  
  
ENV WODBY_DIR_FILES="/mnt/files"  
  
USER root  
  
RUN addgroup -S -g 82 www-data && \  
addgroup nginx www-data && \  
rm /etc/gotpl/default-vhost.conf.tpl && \  
mkdir -p $WODBY_DIR_FILES  
  
USER nginx  
  
COPY templates /etc/gotpl/  
COPY init /docker-entrypoint-init.d/

