FROM php:7.1-alpine  
  
ADD . /code  
WORKDIR /code  
  
ENV SYMFONY_ENV=prod  
ENV SYMFONY_DEBUG=0  
ADD https://getcomposer.org/installer composer-setup.php  
RUN php composer-setup.php && rm composer-setup.php && php composer.phar
install && rm composer.phar  
  
CMD php bin/console report

