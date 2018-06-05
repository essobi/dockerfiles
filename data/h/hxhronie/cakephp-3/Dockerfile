FROM php:7.1.5-apache  
  
LABEL maintainer="Ronie Vincent Horca" \  
maintainer-contact="<ronievincent.gss@gmail.com>"  
  
RUN apt-get update && apt-get install -y \  
libicu-dev \  
libpq-dev \  
libmcrypt-dev \  
mysql-client \  
git \  
zip \  
unzip \  
&& rm -r /var/lib/apt/lists/* \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-install \  
intl \  
mbstring \  
mcrypt \  
pcntl \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
zip \  
opcache  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
ENV APP_HOME=/var/www/html \  
APACHE_RUN_USER=www-data \  
APACHE_RUN_GROUP=www-data \  
APACHE_LOG_DIR=/var/log/apache2 \  
APACHE_PID_FILE=/var/run/apache2.pid \  
APACHE_RUN_DIR=/var/run/apache2 \  
APACHE_LOCK_DIR=/var/lock/apache2 \  
COMPOSER_ALLOW_SUPERUSER=1 \  
COMPOSER_NO_INTERACTION=1  
  
RUN usermod -u 1000 $APACHE_RUN_USER && groupmod -g 1000 $APACHE_RUN_GROUP \  
&& sed -i -e "s/html/html\/webroot/g" /etc/apache2/sites-
enabled/000-default.conf \  
&& a2enmod rewrite  
  
# To copy successfully, add this dockerfile to the root folder  
# Just change the path if ever you want to place the dockerfile in a separate
folder  
COPY . $APP_HOME  
  
RUN composer install \  
&& chown -R $APACHE_RUN_USER:$APACHE_RUN_GROUP $APP_HOME  
  
WORKDIR $APP_HOME  
  
# Adding the following env variables on /var/www/html  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
  
ENTRYPOINT ["sh", "-c", "composer install ; apache2 -DFOREGROUND"]  

