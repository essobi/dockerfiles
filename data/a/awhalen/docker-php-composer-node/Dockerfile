FROM php:5.6-apache  
MAINTAINER Andrew Whalen <github@amwhalen.com>  
  
ENV APACHE_DOCROOT /var/www/html/web  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
  
#  
# Install basic requirements  
#  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
apt-transport-https \  
git \  
build-essential \  
libssl-dev \  
wget \  
unzip \  
bzip2 \  
libbz2-dev \  
zlib1g-dev \  
mysql-client \  
libfontconfig \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libicu-dev \  
libxml2-dev \  
libldap2-dev \  
libmcrypt-dev \  
python-pip \  
fabric \  
jq \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#  
# Install Node (with NPM), and Yarn (via package manager for Debian)  
#  
# https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-
linux-distributions  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get update \  
&& apt-get install -y \  
nodejs  
RUN npm install -g yarn  
  
#  
# Install Composer and Drush  
#  
ENV PATH "/composer/vendor/bin:$PATH"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_VERSION 1.5.2  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer
\  
&& php -r " \  
\$signature =
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& rm /tmp/installer.php \  
&& composer --ansi --version --no-interaction \  
&& composer global require drush/drush --prefer-dist  
  
#  
# WP-CLI  
#  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar  
RUN php wp-cli.phar --info --allow-root  
RUN chmod +x wp-cli.phar  
RUN mv wp-cli.phar /usr/local/bin/wp  
  
#  
# Install additional php extensions  
#  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install -j$(nproc) \  
bcmath \  
bz2 \  
calendar \  
exif \  
ftp \  
gd \  
gettext \  
intl \  
ldap \  
mcrypt \  
mysqli \  
opcache \  
pcntl \  
pdo_mysql \  
shmop \  
soap \  
sockets \  
sysvmsg \  
sysvsem \  
sysvshm \  
zip  
  
#  
# PHP xdebug for phpunit code coverage report  
#  
RUN pecl update-channels \  
&& pecl install xdebug-2.5.5 \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> $PHP_INI_DIR/conf.d/xdebug.ini  
  
#  
# PHP configuration  
#  
# Set timezone  
RUN echo "date.timezone = \"America/New_York\"" >
$PHP_INI_DIR/conf.d/timezone.ini  
# Increase PHP memory limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/timezone.ini  
# Set upload limit  
RUN echo "upload_max_filesize = 128M\npost_max_size = 128M" >
$PHP_INI_DIR/conf.d/00-max_filesize.ini  
  
#  
# Apache configuration  
#  
RUN a2enmod rewrite headers expires ssl \  
&& sed -i "/User www-data/c\User \$\\{APACHE_RUN_USER\\}"
/etc/apache2/apache2.conf \  
&& sed -i "/Group www-data/c\Group \$\\{APACHE_RUN_GROUP\\}"
/etc/apache2/apache2.conf \  
&& sed -i "/DocumentRoot \/var\/www\/html/c\\\\\tDocumentRoot
\$\\{APACHE_DOCROOT\\}" /etc/apache2/sites-enabled/000-default.conf \  
# Preemptively add a user 1000, for use with $APACHE_RUN_USER on osx  
&& adduser --uid 1000 \--gecos 'My OSX User' \--disabled-password osxuser  
  
  
#  
# Python: mkdocs  
#  
RUN pip install mkdocs  
  
COPY test.sh /test.sh

