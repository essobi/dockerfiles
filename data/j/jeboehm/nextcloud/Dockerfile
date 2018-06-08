ARG PHP_VER=7.2  
ARG NEXTCLOUD_VER=13.0  
FROM nextcloud:${NEXTCLOUD_VER}-fpm AS nextcloud  
  
FROM jeboehm/php-nginx-base:${PHP_VER}  
LABEL maintainer="jeff@ressourcenkonflikt.de"  
  
RUN apk add --no-cache \  
bash \  
coreutils \  
findutils \  
rsync && \  
docker-php-ext-install pcntl  
  
COPY \--from=nextcloud /usr/local/etc/php/conf.d/opcache-recommended.ini
/usr/local/etc/php/conf.d/opcache.ini  
COPY \--from=nextcloud /entrypoint.sh /entrypoint.sh  
COPY \--from=nextcloud /usr/src/nextcloud /usr/src/nextcloud  
COPY nginx.conf /etc/nginx/sites-enabled/10-docker.conf  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

