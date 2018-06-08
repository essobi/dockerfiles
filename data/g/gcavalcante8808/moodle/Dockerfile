from php:7.0-apache  
RUN apt-get update && \  
apt-get install --no-install-recommends -y git \  
libpq-dev \  
tar \  
locales \  
libpng-dev \  
libjpeg-dev \  
libxml2-dev \  
libicu-dev \  
libldap2-dev \  
wget \  
ghostscript && \  
sed -i 's/# pt_BR.UTF-8/pt_BR.UTF8/' /etc/locale.gen && \  
locale-gen && \  
ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get clean  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 /usr/bin/dumb-init  
  
COPY files/install-composer.sh /  
  
RUN chmod +x /usr/bin/dumb-init && \  
bash /install-composer.sh && \  
docker-php-ext-install pdo_pgsql mysqli pgsql zip gd xmlrpc soap intl opcache
ldap json && \  
pecl install redis && \  
a2enmod rewrite && a2enmod ssl  
  
COPY files/moodle.conf /etc/apache2/sites-available/default.conf  
COPY files/moodle.php.ini /usr/local/etc/php/conf.d/moodle.ini  
COPY files/redis.ini /usr/local/etc/php/conf.d/redis.ini  
COPY files/docker-entrypoint.sh /entrypoint  
  
WORKDIR /var/www/html  
ENTRYPOINT ["/usr/bin/dumb-init","/entrypoint"]  
CMD ["run"]  

