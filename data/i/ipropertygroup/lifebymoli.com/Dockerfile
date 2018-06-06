FROM ipropertygroup/webserver:nginx-php-5  
MAINTAINER MOHSEN@IPROPERTY  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY . /var/www/html  
COPY docker/lifebymoli.nginx /etc/nginx/conf.d/default.conf  
COPY docker/lifebymolic.rt /etc/nginx/conf.d/lifebymoli.crt  
COPY docker/lifebymolip.em /etc/nginx/conf.d/lifebymoli.key  
COPY docker/php.ini /usr/local/etc/php/conf.d/dev.ini  
COPY docker/docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh && rm -rf /var/www/html/docker
/var/www/html/Dockerfile /var/www/html/.git  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]  

