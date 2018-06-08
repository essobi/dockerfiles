FROM php:5-apache  
  
MAINTAINER nohona <nohona@hotmail.com>  
  
LABEL version 1.0  
LABEL description "SugarCRM Version: SugarCE-Full-6.5.25 base image
php:5-apache"  
  
RUN apt-get update && apt-get install -y \  
zlib1g-dev \  
php5-imap \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
wget \  
unzip \  
&& docker-php-ext-install -j$(nproc) iconv \  
&& docker-php-ext-install -j$(nproc) mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install -j$(nproc) mysql \  
&& docker-php-ext-install -j$(nproc) mysqli \  
&& docker-php-ext-install -j$(nproc) zip \  
&& ln /etc/php5/mods-available/imap.ini /usr/local/etc/php/conf.d/imap.ini \  
&& ln /usr/lib/php5/20131226/imap.so /usr/local/lib/php/extensions/no-debug-
non-zts-20131226/imap.so \  
&& wget https://github.com/certbot/certbot/archive/master.zip -P /usr/local \  
&& unzip /usr/local/master.zip -d /usr/local \  
&& rm /usr/local/master.zip  
  
COPY ./SugarCE-Full-6.5.25 /var/www/html  
COPY ./usr/local/etc/php/php.ini/php.ini /usr/local/etc/php/php.ini  
COPY ./config/.htaccess /var/www/html/.htaccess  
  
VOLUME /etc/apache2  
VOLUME /etc/letsencrypt  
  
RUN chmod 766 /var/www/html/config.php \  
&& chown -R 33:33 /var/www  
  
# To build:  
# docker build --tag <user-name>/sugarcrm:latest .  
# To run:  
# docker run -d -p 8181:80 --name sugarcrm <user-name>/sugarcrm  
# Container shell access:  
# docker exec -it sugarcrm bash  

