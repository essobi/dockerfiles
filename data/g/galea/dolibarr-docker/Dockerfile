FROM php:7.1-apache  
MAINTAINER Joshua LOGAN  
  
ENV VERSION develop  
ENV PHP_TIMEZONE Europe/Paris  
ENV PHP_MEMORY_LIMIT 256M  
ENV MAX_UPLOAD 128M  
  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libldap2-dev
libpq-dev cron wget curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap \  
&& docker-php-ext-install mysqli \  
&& apt-get purge -y libpng12-dev libjpeg-dev libldap2-dev  
  
COPY php.ini /usr/local/etc/php/  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
RUN cd /tmp \  
&& curl -sL "https://github.com/Dolibarr/dolibarr/archive/${VERSION}.tar.gz"
-o dolibarr.tar.gz \  
&& tar -xzf dolibarr.tar.gz \  
&& cp -R dolibarr-$VERSION/htdocs/. /var/www/html \  
&& rm -R dolibarr-$VERSION \  
&& rm dolibarr.tar.gz \  
&& mkdir /var/www/html/documents \  
&& chown -hR www-data:www-data /var/www/html  
  
VOLUME ["/var/www/html/conf", "/var/www/html/documents"]  
  
EXPOSE 80  

