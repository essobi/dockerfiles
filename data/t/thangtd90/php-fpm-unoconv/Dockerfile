FROM framgia/laravel-php-fpm  
  
RUN apt-get update && apt-get install -y --force-yes unoconv libxml2-dev  
  
RUN docker-php-ext-install soap  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

