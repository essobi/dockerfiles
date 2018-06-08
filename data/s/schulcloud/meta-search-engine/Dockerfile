FROM php:7.0-apache  
  
COPY src/ /var/www/html/  
  
COPY meta-search-docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["meta-search-docker-entrypoint.sh"]  
  
CMD ["http://content.schul-cloud.org/v1/search"]  

