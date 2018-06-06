FROM php:5.6-fpm  
  
# Install additional tools:  
RUN apt-get update -qq && apt-get install -yq --no-install-recommends \  
mysql-client \  
nano \  
vim \  
wget \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
git \  
golang-go \  
bzip2 \  
gettext \  
libmemcached-dev \  
zlib1g-dev \  
libmhash2 \  
libxml2-dev \  
libgmp-dev \  
patch \  
zip \  
unzip \  
rsync \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& pecl install memcache-2.2.7 \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring opcache pdo pdo_mysql pdo_pgsql zip
bcmath calendar exif gettext gmp mysql mysqli pcntl sockets shmop sysvmsg
sysvsem sysvshm \  
  
# Install Xdebug support:  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
  
# Install Mailhog Sendmail support (requires git and golang-go)  
&& mkdir -p /opt/go \  
&& export GOPATH=/opt/go \  
&& go get github.com/mailhog/mhsendmail  
  
# Copy PHP configs  
COPY conf.d/* /usr/local/etc/php/conf.d/  
RUN chmod 644 /usr/local/etc/php/conf.d/* \  
&& chgrp staff /usr/local/etc/php/conf.d/* \  
&& mkdir -p /var/log/simplesaml \  
&& chown -Rf www-data:www-data /var/log/simplesaml \  
&& chmod a+rw /var/log/simplesaml \  
  
## Adds private and temp directories  
&& mkdir -p /var/www/private \  
&& mkdir -p /var/www/tmp  
  
# Copy the drush alias file...  
# Add default drush aliases  
RUN mkdir -p /var/www/.drush  
COPY default.aliases.drushrc.php /var/www/.drush/default.aliases.drushrc.php  
  
# Register the COMPOSER_HOME environment variable  
# Add global binary directory to PATH and make sure to re-export it  
# Allow Composer to be run as root  
# Composer version  
ENV COMPOSER_HOME /composer  
ENV PATH /composer/vendor/bin:$PATH  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_VERSION 1.3.0  
# Setup the Composer installer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
  
# Install Composer  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php \  
# Install Prestissimo plugin for Composer -- allows for parallel processing of
packages during install / update  
&& composer global require "hirak/prestissimo:^0.3" \  
&& chown -Rf www-data:www-data /composer \  
&& chown -Rf www-data:www-data /var/www  
  
WORKDIR /var/www/html  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN chmod a+x /usr/local/bin/docker-entrypoint.sh  
  
## Martin County specific customizations:  
RUN mkdir -p /mnt/files/martin.prod/sites/default/files-private \  
&& chown -Rf www-data:www-data /mnt/files/martin.prod/sites/default/files-
private \  
&& chmod 700 /mnt/files/martin.prod/sites/default/files-private \  
&& mkdir -p /mnt/tmp/martin \  
&& chmod 750 /mnt/tmp/martin \  
&& chown -Rf www-data:www-data /mnt/tmp/martin  
  
USER www-data  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["php-fpm"]  

