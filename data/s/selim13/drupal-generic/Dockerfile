FROM php:5.6-apache  
  
MAINTAINER Dmitry Seleznyov <selim013@gmail.com>  
  
RUN a2enmod rewrite expires  
RUN usermod -u 1000 www-data  
  
# install the PHP extensions we need  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libcurl3-gnutls-dev \  
libjpeg-dev \  
libpng12-dev \  
libxml2-dev \  
curl \  
imagemagick \  
git \  
msmtp \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install curl gd json mysqli pdo_mysql opcache zip xml  
  
COPY php/opcache-recomended.ini /usr/local/etc/php/conf.d/  
  
# Composer  
ENV COMPOSER_VERSION 1.2.0  
ENV COMPOSER_HOME /composer  
ENV PATH /composer/vendor/bin:$PATH  
ENV COMPOSER_ALLOW_SUPERUSER 1  
# Setup the Composer installer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} \  
&& rm -rf /tmp/composer-setup.php  
  
# Drush  
ENV DRUSH_VERSION 7.3.0  
RUN composer global require drush/drush:"$DRUSH_VERSION" \--prefer-dist  
  
VOLUME /var/www/html  
  
CMD ["apache2-foreground"]  

