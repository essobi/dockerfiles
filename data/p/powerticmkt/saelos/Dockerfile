FROM php:7.1-apache  
  
LABEL maintainer="Luiz Eduardo <luiz@powertic.com>"  
# Install PHP extensions  
RUN apt-get update && apt-get install --no-install-recommends -y \  
build-essential \  
libicu-dev \  
cron \  
libc-client-dev \  
libicu-dev \  
libkrb5-dev \  
libmcrypt-dev \  
libpq-dev \  
libssl-dev \  
git \  
zip \  
mysql-client \  
unzip \  
g++ \  
libmagickwand-dev \  
imagemagick \  
libpng-dev \  
zlib1g-dev \  
libzip-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
wget \  
curl \  
libmcrypt-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& docker-php-ext-install mbstring intl zip gd exif \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-install \  
intl \  
mbstring \  
mcrypt \  
pcntl \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
zip \  
opcache \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
RUN pecl install imagick -y  
  
RUN docker-php-ext-enable imagick  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
  
RUN apt-get install -y nodejs  
  
# Put apache config for Laravel  
COPY docker-apache/apache2-laravel.conf /etc/apache2/sites-
available/laravel.conf  
  
RUN a2dissite 000-default.conf && a2ensite laravel.conf && a2enmod rewrite  
  
VOLUME /var/www/html  
  
WORKDIR /var/www/html  
  
COPY docker-apache/docker-php-entrypoint.sh /entrypoint.sh  
  
RUN ["chmod", "+x", "/entrypoint.sh"]  
  
EXPOSE 80  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["apache2-foreground"]  

