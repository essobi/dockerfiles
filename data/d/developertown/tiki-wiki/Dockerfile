FROM php:5.6-apache  
# (Tiki is not certified for PHP 7.x yet as of Tiki 17.1)  
ENV TIKI_RELEASE "Tiki_17.x_Zeta_Bootis"  
ENV TIKI_VERSION "17.1"  
RUN apt-get update  
RUN apt-get install -y \  
libmysqlclient-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
cron \  
vim  
  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd  
  
RUN a2enmod rewrite  
  
WORKDIR /opt  
RUN curl -L \  
https://downloads.sourceforge.net/project/tikiwiki/${TIKI_RELEASE}/${TIKI_VERSION}/tiki-${TIKI_VERSION}.tar.gz
\  
| tar -xzf -  
RUN mv "/opt/tiki-${TIKI_VERSION}" /opt/tiki-distribution  
RUN mkdir /opt/tiki  
  
# Setup crontab (only used with the CMD is `cron -f`)  
RUN \  
echo "* * * * * /usr/local/bin/php /opt/tiki/console.php scheduler:run" >
/opt/tiki-crontab \  
&& crontab -u www-data /opt/tiki-crontab  
  
# Update Apache config to use alternate DocumentRoot  
ENV APACHE_DOCUMENT_ROOT "/opt/tiki"  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  
  
COPY tiki-entrypoint /usr/local/bin  
ENTRYPOINT ["tiki-entrypoint"]  
WORKDIR /opt/tiki

