FROM rtancman/php:5.6-fpm-dev-memcached  
  
COPY phpfpm-foreground /usr/local/bin/  
  
RUN apt-get update \  
&& apt-get install -y \  
mysql-client libmysqlclient-dev \  
postgresql-client libpq-dev \  
sqlite3 libsqlite3-dev \  
ldap-utils libldb-dev libldap2-dev \  
&& yes '' | pecl install -f zendopcache-7.0.2 \  
&& yes '' | pecl install -f apcu \  
&& echo "extension=apcu.so" >> /usr/local/etc/php/conf.d/apcu.ini \  
&& yes '' | pecl install -f APCu-4.0.10 \  
&& yes '' | pecl install -f mongo \  
&& echo "extension=mongo.so" >> /usr/local/etc/php/conf.d/mongo.ini \  
&& yes '' | pecl install -f mongodb \  
&& echo "extension=mongodb.so" >> /usr/local/etc/php/conf.d/mongodb.ini \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install iconv mcrypt mysql \  
gd zip pdo pdo_mysql soap shmop sockets sysvmsg sysvsem \  
sysvshm pcntl mbstring gettext exif dba bcmath calendar bz2 \  
wddx mysqli pgsql pdo_pgsql pdo_sqlite opcache \  
&& docker-php-ext-configure wddx \  
&& ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \  
&& docker-php-ext-install ldap \  
&& chmod +x /usr/local/bin/phpfpm-foreground \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www/html  
  
EXPOSE 9004  
EXPOSE 9000  
  
ENTRYPOINT ["/usr/local/bin/phpfpm-foreground"]

