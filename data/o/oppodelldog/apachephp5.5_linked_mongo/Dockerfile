FROM ubuntu:14.04  
VOLUME ["/var/www"]  
  
RUN apt-get update && \  
apt-get install -y \  
apache2 \  
php5 \  
php5-cli \  
libapache2-mod-php5 \  
php5-gd \  
php5-json \  
php5-ldap \  
php5-mysql \  
php5-pgsql \  
php5-dev \  
libcurl4-openssl-dev \  
pkg-config \  
libssl-dev \  
libsslcommon2-dev \  
libpcre3-dev \  
php-pear  
  
COPY build/apache_default /etc/apache2/sites-available/000-default.conf  
COPY build/run /usr/local/bin/run  
COPY build/php.ini /etc/php5/apache2/  
RUN pecl install mongo  
RUN chmod +x /usr/local/bin/run  
RUN a2enmod rewrite  
  
EXPOSE 80  
CMD ["/usr/local/bin/run"]  

