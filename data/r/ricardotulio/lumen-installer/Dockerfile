FROM composer  
  
ENV COMPOSER_HOME /composer  
  
RUN mkdir /composer  
RUN composer global require laravel/lumen-installer  
  
ENTRYPOINT ["/composer/vendor/bin/lumen"]  

