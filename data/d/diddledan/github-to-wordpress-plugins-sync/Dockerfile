FROM php:7.0-apache  
  
RUN ln -sfT /dev/stderr /var/www/push.log && mkdir -p /var/www/wpsync-svns &&
chown www-data:www-data /var/www/wpsync-svns  
RUN apt-get update && apt-get install -yqq subversion && apt-get clean && rm
-rf /var/lib/apt/lists/*  
  
COPY WordPress-sync-docker-entrypoint /usr/local/bin/  
  
COPY config-sample.php /var/www/html/config.php  
RUN sed -i 's!^\\(\$svns_location = \\).*$!\1"/var/www/wpsync-svns/";!'
/var/www/html/config.php && \  
sed -i 's!^\\(\$save_log = \\).*$!\1"/var/www/push.log";!'
/var/www/html/config.php  
  
COPY *.php /var/www/html/  
  
ENTRYPOINT ["WordPress-sync-docker-entrypoint"]  
CMD ["apache2-foreground"]

