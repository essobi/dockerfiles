FROM wordpress:4.3.1-fpm  
MAINTAINER Mike Green <mike.is.green@gmail.com>  
  
RUN apt-get -y update && apt-get -y install less wget  
  
# Install WP-CLI  
RUN wget -O /usr/local/bin/wp https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar && chmod +x /usr/local/bin/wp  
  
# Install XDebug extension  
WORKDIR /tmp  
RUN wget -O xdebug.tgz http://xdebug.org/files/xdebug-2.3.3.tgz && tar xzf
xdebug.tgz  
WORKDIR /tmp/xdebug-2.3.3  
RUN phpize && ./configure && make  
RUN cp modules/xdebug.so /usr/local/lib/php/extensions/no-debug-non-
zts-20131226/  
RUN rm -rf /tmp/xdebug*  
  
# Add custom php.ini  
COPY config/php.ini /usr/local/etc/php/  

