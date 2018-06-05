FROM php:7-apache  
  
MAINTAINER Simon Morvan <simon@icilalune.com>  
  
ADD docker/docker-php-pecl-install /usr/local/bin/  
  
RUN echo "APT::Install-Recommends \"0\";" >> /etc/apt/apt.conf.d/02recommends
\  
&& echo "APT::Install-Suggests \"0\";" >> /etc/apt/apt.conf.d/02recommends \  
&& apt-get update && apt-get install -y \  
git \  
imagemagick \  
libcurl4-openssl-dev \  
libedit-dev \  
libfreetype6-dev \  
libjpeg-turbo-progs \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
libsqlite3-dev \  
libxml2-dev \  
mysql-client \  
postgresql-client \  
pngquant \  
ssmtp \  
sudo \  
sqlite \  
unzip \  
wget \  
zlib1g-dev \  
&& apt-get clean && apt-get autoremove -q \  
&& rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man /tmp/* \  
&& docker-php-ext-install \  
bcmath \  
curl \  
exif \  
mbstring \  
mcrypt \  
mysqli \  
opcache \  
pcntl \  
pdo_mysql \  
pdo_pgsql \  
pdo_sqlite \  
pgsql \  
readline \  
zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& cd /usr/local \  
&& curl -sS https://getcomposer.org/installer | php \  
&& chmod +x /usr/local/composer.phar \  
&& ln -s /usr/local/composer.phar /usr/local/bin/composer \  
&& sed 's,Listen 80,Listen 8080,g' -i /etc/apache2/apache2.conf \  
&& echo "sendmail_path = /usr/sbin/ssmtp -t" > /usr/local/etc/php/conf.d/conf-
sendmail.ini \  
&& echo "date.timezone='Europe/Paris'\n" > /usr/local/etc/php/conf.d/conf-
date.ini  
  
RUN docker-php-pecl-install \  
apcu  
  
COPY docker/env.template /app/.env  
COPY docker/entrypoint.sh /sbin/entrypoint.sh  
  
USER root  
  
RUN chmod +x /sbin/entrypoint.sh  
  
ADD . /app  
  
RUN chown www-data:www-data -R /app \  
&& rm -rf /var/www/html \  
&& ln -s /app/public /var/www/html  
  
WORKDIR /app  
USER www-data  
  
RUN composer install --no-dev -o \  
&& rm -rf bootstrap/cache/*  
  
EXPOSE 8080  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
  
CMD ["start"]  

