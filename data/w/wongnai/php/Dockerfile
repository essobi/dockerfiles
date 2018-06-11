FROM php:7.0.13-apache  
  
MAINTAINER Suparit Krityakien <suparit@wongnai.com>  
  
RUN a2enmod rewrite expires headers  
  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache \  
&& { \  
echo 'opcache.memory_consumption=192'; \  
echo 'opcache.interned_strings_buffer=32'; \  
echo 'opcache.max_accelerated_files=10000'; \  
echo 'opcache.revalidate_freq=120'; \  
echo 'opcache.validate_timestamps=0'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
WORKDIR /var/www/html  
  
#VOLUME ["/var/www/html"]  
EXPOSE 80  
CMD ["apache2-foreground"]  

