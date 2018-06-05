FROM php:5.6-fpm  
  
LABEL MAINTAINER="Greg Junge <gregnuj@gmail.com>"  
  
## Install project requirements  
RUN apt-get update \  
&& apt-get install -y \  
bash \  
curl \  
git \  
zip \  
unzip \  
unixodbc-dev \  
libpq-dev \  
libicu-dev \  
libmcrypt-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
## Install project php extensions  
RUN docker-php-ext-configure pdo_odbc --with-pdo-odbc=unixODBC,/usr/ \  
&& docker-php-ext-install \  
mcrypt \  
mbstring \  
pdo_mysql \  
pdo_pgsql \  
intl \  
zip  
#pdo_oci  
## Set up php enviroment  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
## Set up composer enviroment  
ENV PATH="/composer/vendor/bin:$PATH" \  
COMPOSER_ALLOW_SUPERUSER=1 \  
COMPOSER_HOME=/composer \  
COMPOSER_VERSION=1.3.3  
## Install composer  
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
&& composer self-update \  
&& composer --ansi --version --no-interaction  
  
## Set up project enviroment  
ENV PROJECT_WORKDIR="/var/www/html/app" \  
PROJECT_NAME="cakephp/cakephp:2.9.*" \  
PROJECT_VCS=""  
## Listen on tcp port 9000  
RUN sed -i -e 's/listen.*/listen = 0.0.0.0:9000/' /usr/local/etc/php-fpm.conf  
EXPOSE 9000  
COPY docker-composer-entrypoint /usr/local/bin/docker-composer-entrypoint  
RUN chmod 755 /usr/local/bin/docker-composer-entrypoint  
ENTRYPOINT ["/usr/local/bin/docker-composer-entrypoint"]  
CMD ["php-fpm"]  
  

