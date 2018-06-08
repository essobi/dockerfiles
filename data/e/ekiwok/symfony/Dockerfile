FROM php:7.1-fpm  
  
COPY base.ini /usr/local/etc/php/conf.d/  
COPY scripts/entrypoint.sh /usr/bin/entrypoint.sh  
COPY scripts/setup.sh setup.sh  
  
RUN chmod +x /usr/bin/entrypoint.sh setup.sh && ./setup.sh && rm -f setup.sh  
  
WORKDIR /var/www  
  
CMD "/usr/bin/entrypoint.sh"

