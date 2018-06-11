FROM php:5.6-fpm  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt mbstring \  
&& docker-php-ext-install zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
# Install composer  
RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf && curl -sS
https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN chmod +x /usr/local/bin/composer  
  
# RUN pecl install redis  
# RUN echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini  
# Install Git  
RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf && apt-get install -y git  
  
WORKDIR /code  
  
CMD ["/usr/local/bin/composer", "install"]  

