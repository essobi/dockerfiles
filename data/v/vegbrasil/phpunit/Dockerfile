FROM php:cli  
MAINTAINER David Bingham  
MAINTAINER Vinícius Santana <vinicius@vegbrasil.com>  
  
# Utilities  
RUN apt-get update && apt-get install -y wget  
  
# MySQLi  
RUN docker-php-ext-install mysqli  
  
# PHPUnit  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
RUN phpunit --version  
  
# XDebug  
RUN pecl install xdebug  
RUN echo
"zend_extension=xdebug.so\nxdebug.cli_color=1\nxdebug.remote_autostart=1\nxdebug.remote_connect_back=1"
> /usr/local/etc/php/conf.d/xdebug.ini  
  
# Volume and Workdir  
VOLUME ["/app"]  
WORKDIR /app  
  
# Entrypoint  
ENTRYPOINT ["/usr/local/bin/phpunit"]  
CMD ["--help"]  

