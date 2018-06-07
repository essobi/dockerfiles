FROM php:fpm  
  
RUN ln -s /app /var/www/html  
  
RUN apt-get update && apt-get install -y \  
libssl-dev \  
&& apt-get clean \  
&& pecl install mongo \  
&& echo 'extension=mongo.so' > /usr/local/etc/php/conf.d/mongo.ini  

