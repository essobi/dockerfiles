FROM nextcloud:13.0.2-fpm  
RUN apt-get update && \  
apt-get install htop -y  
  
COPY config.sh /  
COPY hoffmann /var/www/html/themes/hoffmann  
COPY demo /var/www/html/themes/demo  
COPY tst /var/www/html/themes/tst  
RUN chmod +x /config.sh  
ENTRYPOINT ["/config.sh"]  
CMD ["php-fpm"]

