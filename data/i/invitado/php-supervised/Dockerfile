FROM php:7.2-alpine  
  
# Install needed PHP extensions.  
RUN apk add --update libpng-dev && rm -rf /var/cache/apk/*  
RUN docker-php-ext-install pdo_mysql sockets bcmath gd  
  
# Install S6.  
RUN apk add --update s6 && rm -rf /var/cache/apk/*  
COPY s6 /opt/s6  
  
# Add entrypoint script.  
COPY ./entrypoint.sh /opt/entrypoint.sh  
RUN chmod +x /opt/entrypoint.sh  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["/dev/true"]  

