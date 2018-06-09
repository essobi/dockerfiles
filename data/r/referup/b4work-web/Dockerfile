FROM php:5.6-apache  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
mcrypt \  
php5-cli \  
php5-curl \  
php5-mcrypt \  
php5-imap \  
msmtp-mta \  
libmagic-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD index.php /var/www/html/  
ADD msmtprc /etc/msmtprc  
  
RUN a2enmod rewrite  
RUN docker-php-ext-install pdo pdo_mysql  
  
RUN php5enmod mcrypt  
  
COPY mail.ini /usr/local/etc/php/apache2/conf.d/  
  
RUN mkdir -p /usr/local/etc/php/apache2 && \  
cp -R /usr/local/etc/php/conf.d /usr/local/etc/php/apache2 && \  
echo 'export PHP_INI_SCAN_DIR=/usr/local/etc/php/apache2/conf.d' >>
/etc/apache2/envvars  

