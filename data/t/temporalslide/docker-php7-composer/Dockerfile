FROM temporalslide/docker-php7-fpm-alpine:latest  
  
RUN apk add --update bash tini && rm -rf /var/cache/apk/*  
RUN echo "xdebug.remote_enable=off" > /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
  
COPY \--from=composer:1.5 /usr/bin/composer /usr/bin/composer  
COPY \--from=composer:1.5 /docker-entrypoint.sh /docker-entrypoint.sh  
  
WORKDIR /var/www  
  
RUN composer global require hirak/prestissimo  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["composer"]  
  
#CMD ["/usr/bin/composer"]  

