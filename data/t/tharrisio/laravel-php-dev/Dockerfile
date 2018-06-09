FROM tharrisio/laravel-php  
  
RUN apt-get -yqq update \  
&& apt-get install -y --no-install-recommends \  
gnupg \  
git \  
;  
  
RUN curl --silent --location https://deb.nodesource.com/setup_8.x | bash -  
  
RUN apt-get -yqq update \  
&& apt-get install -y --no-install-recommends \  
nodejs \  
sqlite3 \  
libsqlite3-dev \  
libzip-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
;  
  
RUN npm install -g yarn  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer \  
;  
  
RUN pecl install xdebug-2.6.0 \  
&& pecl install zip \  
&& docker-php-ext-enable xdebug zip \  
&& pecl install mongodb \  
&& echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/ext-mongodb.ini \  
;  
  
COPY xdebug.ini /usr/local/etc/php/conf.d/  
  
WORKDIR /app  

