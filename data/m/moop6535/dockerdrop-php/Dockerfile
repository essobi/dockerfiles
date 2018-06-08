FROM php:7.0-fpm  
  
MAINTAINER Lisa Ridley "lhridley@gmail.com"  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
unzip \  
zip \  
mariadb-client \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install pdo_mysql zip opcache bz2  
  
# Register the COMPOSER_HOME environment variable  
# Add global binary directory to PATH and make sure to re-export it  
# Allow Composer to be run as root  
# Composer version  
ENV COMPOSER_HOME /composer  
ENV PATH /composer/vendor/bin:$PATH  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_VERSION 1.2.3  
  
# Setup the Composer installer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) \  
!== trim(file_get_contents('/tmp/composer-setup.sig'))) \  
{ unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . \  
PHP_EOL; exit(1); }" \  
  
# Install Composer  
&& php /tmp/composer-setup.php \--no-ansi --install-dir=/usr/local/bin \  
\--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php \  
# Install Prestissimo plugin for Composer \-- allows for parallel processing
of  
# packages during install / update  
&& composer global require "hirak/prestissimo:^0.3" \  
&& chown -Rf www-data:www-data /composer \  
&& chown -Rf www-data:www-data /var/www \  
# Install Drush  
&& mkdir /usr/local/drush \  
&& cd /usr/local/drush \  
&& composer init \--require=drush/drush:8.* -n \  
&& composer config bin-dir /usr/local/bin \  
&& composer install \  
&& drush init -y \  
# Set up default location for drush alias files  
&& mkdir -p /etc/drush/site-aliases  
  
# Copy drush alias file into image  
COPY default.aliases.drushrc.php /etc/drush/site-aliases/  
  
# Install Mailhog Sendmail support:  
RUN apt-get update -qq && apt-get install -yq git golang-go \  
&& mkdir -p /opt/go \  
&& export GOPATH=/opt/go \  
&& go get github.com/mailhog/mhsendmail  
  
# Add php.ini base file  
COPY php.ini /usr/local/etc/php/conf.d/php.ini  
  
# Add entrypoint script  
COPY docker-entrypoint.sh /usr/local/bin/  
# Make sure it's executable  
RUN chmod a+x /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
CMD ["php-fpm"]

