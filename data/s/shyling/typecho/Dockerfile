FROM php:apache  
  
RUN apt-get -y update \  
&& apt-get -y install libcurl4-openssl-dev libxml2-dev libfreetype6-dev
libjpeg62-turbo-dev libmcrypt-dev libpng12-dev libpq-dev  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) curl dom exif fileinfo gd iconv json
mbstring mcrypt mysqli opcache pcntl pdo pdo_mysql pdo_pgsql pgsql session
sockets xml xmlrpc zip  
  
COPY . /var/www/html  
RUN chown -R www-data:www-data /var/www/html  
  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
RUN sed -i "s/AllowOverride None/AllowOverride All/" /etc/apache2/apache2.conf
\  
&& a2enmod rewrite expires  

