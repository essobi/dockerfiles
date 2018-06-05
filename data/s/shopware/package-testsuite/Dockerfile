FROM php:5.6-apache  
  
ADD php/_010_php.ini /usr/local/etc/php/conf.d/  
  
RUN mkdir -p /etc/apache2/sites-available \  
&& mkdir -p /etc/ssl/certs/ \  
&& mkdir -p /var/www/cdn  
  
COPY ioncube/ioncube_loader_lin_5.6.so /var/ioncube/  
COPY sites-available/000-default.conf /etc/apache2/sites-
available/000-default.conf  
COPY sites-available/001-assetgenerator.conf /etc/apache2/sites-
available/001-assetgenerator.conf  
COPY sites-available/002-updates.conf /etc/apache2/sites-
available/002-updates.conf  
COPY sites-available/003-cdn.conf /etc/apache2/sites-available/003-cdn.conf  
COPY ssl/cert.txt /etc/ssl/certs/cert.txt  
COPY ssl/key.txt /etc/ssl/certs/key.txt  
COPY cdn/.htaccess /var/www/cdn/.htaccess  
  
  
RUN apt-get update && apt-get install --no-install-recommends -y \  
openjdk-7-jre-headless \  
ant \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zip \  
zlib1g-dev \  
unzip \  
mysql-client \  
ssmtp \  
wget \  
tar \  
libcurl4-gnutls-dev \  
curl \  
libxml2 \  
libxml2-dev \  
openssl \  
libssl-dev \  
netcat \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mysqli \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install ftp \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install curl \  
&& docker-php-ext-install pdo pdo_mysql \  
&& echo "sendmail_path = /usr/sbin/ssmtp -t" >
/usr/local/etc/php/conf.d/_011_sendmail.ini \  
&& echo "mailhub=smtp:1025\nUseTLS=NO\nFromLineOverride=YES" >
/etc/ssmtp/ssmtp.conf \  
&& cd /var/www \  
&& echo "zend_extension = /var/ioncube/ioncube_loader_lin_5.6.so" >
/usr/local/etc/php/conf.d/_000_ioncube.ini \  
&& echo "date.timezone = 'Europe/Berlin'" >> /usr/local/etc/php/php.ini \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php \  
&& mv composer.phar /usr/local/bin/composer \  
&& a2enmod vhost_alias \  
&& a2enmod rewrite \  
&& a2enmod ssl \  
&& a2ensite 000-default \  
&& a2ensite 001-assetgenerator \  
&& a2ensite 002-updates \  
&& a2ensite 003-cdn \  
&& wget http://shopwarelabs.github.io/sw-cli-tools/sw.phar \  
&& mv sw.phar /usr/local/bin/sw \  
&& chmod 777 /usr/local/bin/sw \  
&& chmod 777 /usr/local/bin \  
&& mkdir -p /var/www/shopware \  
&& mkdir -p /var/www/updates \  
&& chown -R www-data /var/www \  
&& chmod -R 777 /var/www  
  
WORKDIR /var/www/shopware

