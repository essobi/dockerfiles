FROM php:5.6-fpm  
# Install modules  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install mcrypt  
  
# install from pear  
RUN pear install Net_SMTP Mail  
  
EXPOSE 9000  
CMD ["php-fpm"]  

