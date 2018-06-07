# PHPSpec Docker Container  
FROM composer/composer:alpine  
MAINTAINER Julien Breux <julien.breux@gmail.com>  
  
# Goto temporary directory  
WORKDIR /tmp  
  
# Run composer and phpspec installation.  
RUN composer selfupdate && \  
composer require "phpspec/phpspec:~2.5.2" \--dev && \  
ln -s /tmp/vendor/bin/phpspec /usr/local/bin/phpspec  
  
# Set up the application directory.  
VOLUME ["/app"]  
WORKDIR /app  
  
# Set up the command arguments.  
ENTRYPOINT ["/usr/local/bin/phpspec"]  
CMD ["--help"]  

