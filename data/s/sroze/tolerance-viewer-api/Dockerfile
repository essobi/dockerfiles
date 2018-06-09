FROM sroze/php:7.0-apache  
  
COPY . /app  
WORKDIR /app  
  
RUN rm -rf var/cache/* var/logs/* && \  
composer install && \  
chown www-data .  
  
CMD ["/app/docker/run.sh"]  

