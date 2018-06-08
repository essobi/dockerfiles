FROM php:7-apache  
MAINTAINER Mikael Kermorgant <mikael@kgtech.fi>  
  
VOLUME ["/var/moodledata"]  
EXPOSE 80 443  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
ssmtp \  
cron \  
mysql-client \  
libpng-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libicu-dev \  
libxml2-dev \  
libssl-dev \  
curl \  
libxslt-dev \  
libxml2-dev \  
libzzip-dev \  
libldap2-dev \  
zlib1g-dev \  
libbz2-dev \  
libpspell-dev \  
libpcre3-dev \  
libexif-dev \  
libssh2-1-dev \  
libsnmp-dev \  
libxslt1-dev \  
libxslt-dev \  
libcurl4-openssl-dev \  
libpng++-dev \  
libvpx-dev \  
libtidy-dev \  
libmagic-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install json simplexml \  
&& docker-php-ext-install ctype xml mbstring intl \  
&& docker-php-ext-install gd curl \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-install pdo pdo_mysql \  
&& docker-php-ext-install mysqli soap gettext calendar zip \  
&& docker-php-ext-install xmlrpc opcache  
  
RUN mkdir -p /usr/src/moodle \  
&& curl -SL https://download.moodle.org/download.php/direct/stable31/moodle-
latest-31.tgz \  
| tar -xzC /usr/src/moodle --strip=1  
  
RUN mkdir /var/www/moodle  
VOLUME /var/www/moodle  
WORKDIR /var/www/moodle  
  
COPY entrypoint.sh /entrypoint.sh  
ADD https://raw.githubusercontent.com/kermorgant/docker-
tools/master/lib/dblib.sh /opt/kgtech/dblib.sh  
ADD https://raw.githubusercontent.com/kermorgant/docker-tools/master/bin/wait-
for-it.sh /usr/local/bin/wait-for-it.sh  
  
RUN chmod +x /entrypoint.sh /usr/local/bin/wait-for-it.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["apache2-foreground"]  

