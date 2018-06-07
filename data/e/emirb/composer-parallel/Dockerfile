FROM php:7-alpine  
  
# Based on https://hub.docker.com/r/sarteam/composer/  
MAINTAINER Emir Beganovic <beganovic.emir@gmail.com>  
  
# Packages  
RUN apk --update add \  
git \  
unzip && \  
apk del build-base && \  
rm -rf /var/cache/apk/*  
  
# Memory Limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN chmod a+x /usr/local/bin/composer  
  
RUN mkdir /.composer && chmod 777 -R /.composer  
  
WORKDIR /.composer  
  
# Require composer globally  
RUN composer require hirak/prestissimo  
  
ENTRYPOINT ["composer"]  
  

