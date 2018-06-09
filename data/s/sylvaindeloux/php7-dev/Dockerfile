FROM sylvaindeloux/php7-fpm:latest  
MAINTAINER Sylvain Deloux <docker@eax.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN pecl install xdebug && \  
docker-php-ext-enable xdebug && \  
pecl clear-cache && \  
rm -rf /tmp/*  

