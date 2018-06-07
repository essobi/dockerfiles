FROM php:7  
WORKDIR /code  
  
COPY . /code/  
  
RUN apt-get update && apt-get install -y \  
git \  
unzip \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv /code/composer.phar /usr/local/bin/composer \  
&& mv /code/php.ini /usr/local/etc/php/php.ini \  
&& composer install  
  
ENTRYPOINT php /code/src/run.php --data=/data  

