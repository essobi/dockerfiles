FROM php:5.6-apache  
  
COPY 000-default.conf /etc/apache2/sites-available  
  
COPY php.ini /usr/local/etc/php/conf.d  
  
RUN a2enmod rewrite; \  
apt-get update; \  
apt-get upgrade -y; \  
apt-get install libxml2-dev libcurl3-dev libfreetype6-dev libjpeg62-turbo-dev
git locales locales-all fontconfig libfontconfig1 libxrender1 xfonts-base
xfonts-75dpi libc-client-dev libkrb5-dev -y; \  
rm -r /var/lib/apt/lists/*; \  
docker-php-ext-install pdo_mysql; \  
docker-php-ext-install mysqli; \  
docker-php-ext-install gd; \  
docker-php-ext-install soap; \  
docker-php-ext-configure curl; \  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl; \  
docker-php-ext-install imap; \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/; \  
pecl install xdebug-2.5.5; \  
echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" >
/usr/local/etc/php/conf.d/xdebug.ini; \  
echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini; \  
echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
ENV LANG pt_BR.UTF-8  
ENV LC_ALL pt_BR.UTF-8  
ENV LANGUAGE pt_BR:pt  
  
# Install Wkhtmltopdf  
ADD
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.2.1/wkhtmltox-0.12.2.1_linux-
jessie-amd64.deb /tmp/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb  
  
RUN DEBIAN_FRONTEND="noninteractive" chmod a+x /tmp/wkhtmltox-0.12.2.1_linux-
jessie-amd64.deb; \  
dpkg --install /tmp/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb|| true; \  
apt-get -y --force-yes -f install  
  
# Install phpunit  
ADD https://phar.phpunit.de/phpunit-5.phar /  
  
RUN chmod +x /phpunit-5.phar; \  
mv /phpunit-5.phar /usr/local/bin/phpunit  
  
RUN usermod --non-unique --uid 1000 www-data \  
&& groupmod --non-unique --gid 1000 www-data \  
&& chown -R www-data:www-data /tmp  

