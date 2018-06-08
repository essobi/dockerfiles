FROM php:5.6.30-fpm  
MAINTAINER Oleg Kulik <olegkulik1985@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
cron \  
# dev deps for gd  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
# for intl  
libicu-dev \  
# for mcrypt  
libmcrypt-dev \  
# for xsl  
libxslt1-dev \  
# for ldap  
libldap2-dev \  
libldb-dev \  
&& pecl install xdebug \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install \  
bcmath \  
gd \  
intl \  
ldap \  
mbstring \  
mcrypt \  
mysqli \  
opcache \  
pdo_mysql \  
soap \  
xsl \  
zip \  
# clean up  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
# install Ioncube  
WORKDIR /tmp  
RUN curl -o ioncube.tar.gz
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -zxf ioncube.tar.gz \  
&& mv ioncube/ioncube_loader_lin_5.6.so /usr/local/lib/php/extensions/* \  
&& rm -Rf ioncube.tar.gz ioncube \  
&& echo "zend_extension=ioncube_loader_lin_5.6.so" >
/usr/local/etc/php/conf.d/00_docker-php-ext-ioncube_loader_lin_5.6.ini \  
# modify www-data user  
&& usermod -u 1000 www-data \  
&& groupmod -g 1000 www-data \  
# Install composer  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "copy('https://composer.github.io/installer.sig', 'signature');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
trim(file_get_contents('signature'))) { echo 'Installer verified'; } else {
echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
  
COPY docker-php-entrypoint /usr/local/bin/  
  
VOLUME /srv/www  
WORKDIR /srv/www  
  
CMD ["php-fpm"]  

