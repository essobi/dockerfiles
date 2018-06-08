FROM httpd:2.4-alpine  
  
# Add bash to use it in entrypoint script.  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
  
COPY ./drupal.conf /usr/local/apache2/conf/extra/drupal.conf  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod -v +x /usr/local/bin/docker-entrypoint.sh  
  
CMD "docker-entrypoint.sh"  

