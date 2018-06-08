FROM pam79/composer  
  
MAINTAINER Paapa Abdullah Morgan <paapaabdullahm@gmail.com>  
  
WORKDIR /tmp  
  
RUN composer require --dev phpunit/phpunit ^6.1 --no-interaction \  
&& composer require --dev phpunit/php-invoker --no-interaction \  
&& composer require --dev phpunit/dbunit --no-interaction \  
&& ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit  
  
VOLUME ["/app"]  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/bin/phpunit"]  
CMD ["--help"]

