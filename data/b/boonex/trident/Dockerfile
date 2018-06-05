# Trident docker file  
FROM php:5-apache  
  
MAINTAINER dev@boonex.com  
  
# PHP extensions and necessary packages  
RUN apt-get update && apt-get install -y \  
cron \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
sendmail sendmail-bin \  
unzip \  
&& docker-php-ext-install -j$(nproc) exif \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install -j$(nproc) iconv \  
&& docker-php-ext-install -j$(nproc) mbstring \  
&& docker-php-ext-install -j$(nproc) mcrypt \  
&& docker-php-ext-install -j$(nproc) mysql \  
&& docker-php-ext-install -j$(nproc) opcache \  
&& docker-php-ext-install -j$(nproc) pdo \  
&& docker-php-ext-install -j$(nproc) pdo_mysql \  
&& docker-php-ext-install -j$(nproc) zip \  
&& rm -rf /var/lib/apt/lists/*  
  
# User folder  
RUN groupadd -r --gid 2483 trident \  
&& useradd -r --uid 2483 -g trident trident  
  
RUN chown trident:trident /var/www/html /var/www  
  
# Unzip package  
USER trident  
  
WORKDIR /var/www/html  
  
ENV TRIDENT_VERSION 8.0.1  
# Alternative download URL -
https://github.com/boonex/trident/releases/download/${TRIDENT_VERSION}/Trident-v.${TRIDENT_VERSION}.zip  
RUN curl -fSL "http://ci.boonex.com/builds/Trident-v.${TRIDENT_VERSION}.zip"
-o trident.zip \  
&& unzip -o trident.zip \  
&& rm trident.zip \  
&& mv Trident-v.${TRIDENT_VERSION}/* . \  
&& mv Trident-v.${TRIDENT_VERSION}/.htaccess . \  
&& rm -rf "Trident-v.${TRIDENT_VERSION}"  
  
RUN chmod 777 inc cache cache_public logs tmp storage \  
&& chmod +x plugins/ffmpeg/ffmpeg.exe  
  
# Apache configuration  
USER root  
  
RUN echo "memory_limit=192M \n\  
post_max_size=100M \n\  
upload_max_filesize=100M \n\  
error_log=/var/www/php_error.log \n\  
error_reporting=E_ALL & ~E_NOTICE & ~E_DEPRECATED & ~E_STRICT \n\  
display_errors=Off \n\  
log_errors=On \n\  
sendmail_path=/usr/sbin/sendmail -t -i \n\  
date.timezone=UTC" > /var/www/php.ini && chown trident:trident
/var/www/php.ini  
  
RUN touch /var/www/php_error.log \  
&& chown trident:trident /var/www/php_error.log \  
&& chmod 666 /var/www/php_error.log  
  
RUN echo "<VirtualHost *:80> \n\  
DocumentRoot /var/www/html \n\  
PHPINIDir /var/www \n\  
ErrorLog /var/www/error.log \n\  
CustomLog /var/www/access.log combined \n\  
</VirtualHost>" > /etc/apache2/sites-enabled/trident.conf  
  
RUN a2enmod rewrite expires  
  
# Crontab  
RUN echo "* * * * * php -c /var/www /var/www/html/periodic/cron.php" >
/var/www/crontab  
  
RUN chown trident:trident /var/www/crontab \  
&& crontab -u trident /var/www/crontab  
  
# Expose port  
VOLUME /var/www  
  
EXPOSE 80  

