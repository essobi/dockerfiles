FROM php:7.0.6-apache  
  
MAINTAINER Yuri Novik  
  
LABEL Version="1.0" \  
Description="Azure Web App on Linux / App Service \  
Linux+Apache+PHP7+php_imagick+Composer Docker container"  
  
RUN a2enmod rewrite expires  
  
# install the PHP extensions we need  
RUN apt-get update \  
&& apt-get install -y \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
libmcrypt-dev \  
libldap2-dev \  
libldb-dev \  
libicu-dev \  
libgmp-dev \  
libmagickwand-dev \  
&& ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \  
&& ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
opcache \  
pdo \  
pdo_mysql \  
ldap \  
intl \  
mcrypt \  
gmp \  
zip \  
bcmath \  
mbstring \  
pcntl \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& rm -rf /tmp/pear  
  
# RUN php -r "copy('https://getcomposer.org/installer', 'composer-
setup.php');" \  
# && php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
# && php composer-setup.php \  
# && php -r "unlink('composer-setup.php');" \  
# && php composer.phar install --no-dev --no-scripts \  
# && rm composer.phar  
# RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
# Make sure we're installing what we think we're installing!  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot \  
&& rm -f /tmp/composer-setup.*  
  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN { \  
echo 'error_log=/var/log/apache2/php-error.log'; \  
echo 'display_errors=Off'; \  
echo 'log_errors=On'; \  
echo 'display_startup_errors=Off'; \  
echo 'date.timezone=UTC'; \  
} > /usr/local/etc/php/conf.d/php.ini  
  
COPY apache2.conf /etc/apache2/  
COPY init_container.sh /bin/  
  
RUN \  
rm -f /var/log/apache2/* \  
&& rmdir /var/lock/apache2 \  
&& rmdir /var/run/apache2 \  
&& rmdir /var/log/apache2 \  
&& chmod 644 /etc/apache2/apache2.conf \  
&& chmod 777 /var/log \  
&& chmod 777 /var/run \  
&& chmod 777 /var/lock \  
&& rm -rf /var/www/html \  
&& rm -rf /var/log/apache2 \  
&& ln -s /home/site/wwwroot /var/www/html \  
&& ln -s /home/LogFiles /var/log/apache2  
  
EXPOSE 8080  
  
CMD ["/bin/init_container.sh"]  

