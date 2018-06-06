FROM php:7.0-fpm  
  
RUN apt-get update -y && \  
PHP_VERSION=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") && \  
`#====================================================` \  
`# HealthCheck cgi-fcgi` \  
`#====================================================` \  
apt-get install -y --no-install-recommends libfcgi0ldbl && \  
`#====================================================` \  
`# Locale gen` \  
`#====================================================` \  
apt-get install -y --no-install-recommends locales && \  
cat /usr/share/i18n/SUPPORTED > /etc/locale.gen && \  
/usr/sbin/locale-gen && \  
`#====================================================` \  
`# Logs` \  
`#====================================================` \  
mkdir -p /var/log/php/ && \  
ln -sf /dev/stdout /var/log/php/access.log && \  
ln -sf /dev/stderr /var/log/php/error.log && \  
`#====================================================` \  
`# Session Directory` \  
`#====================================================` \  
mkdir -p /var/lib/php/sessions && \  
chown -R www-data.www-data /var/lib/php/sessions && \  
`#====================================================` \  
`# Mysqlnd` \  
`#====================================================` \  
docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd && \  
docker-php-ext-configure mysqli --with-mysqli=mysqlnd && \  
docker-php-ext-install pdo_mysql && \  
docker-php-ext-install mysqli && \  
`#====================================================` \  
`# Intl` \  
`#====================================================` \  
apt-get install -y --no-install-recommends libicu-dev && \  
docker-php-ext-install intl && \  
`#====================================================` \  
`# Zip` \  
`#====================================================` \  
apt-get install -y --no-install-recommends zlib1g-dev && \  
docker-php-ext-install zip && \  
`#====================================================` \  
`# Apcu` \  
`#====================================================` \  
pecl install apcu && \  
docker-php-ext-enable apcu && \  
`#====================================================` \  
`# Opcache` \  
`#====================================================` \  
docker-php-ext-enable opcache && \  
`#====================================================` \  
`# Gd` \  
`#====================================================` \  
apt-get install -y --no-install-recommends libfreetype6-dev libjpeg62-turbo-
dev libpng12-dev && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd && \  
`#====================================================` \  
`# Imagick` \  
`#====================================================` \  
apt-get install -y --no-install-recommends libmagickwand-dev && \  
pecl install imagick && \  
docker-php-ext-enable imagick && \  
`#====================================================` \  
`# Sockets` \  
`#====================================================` \  
docker-php-ext-install sockets && \  
`#====================================================` \  
`# Redis` \  
`#====================================================` \  
pecl install redis && \  
docker-php-ext-enable redis && \  
`#====================================================` \  
`# Bcmath` \  
`#====================================================` \  
docker-php-ext-install bcmath && \  
`#====================================================` \  
`# Mcrypt` \  
`#====================================================` \  
apt-get install -y --no-install-recommends libmcrypt-dev && \  
docker-php-ext-install mcrypt && \  
`#====================================================` \  
`# Imap` \  
`#====================================================` \  
apt-get install -y --no-install-recommends libc-client-dev libkrb5-dev && \  
docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos && \  
docker-php-ext-install imap && \  
`#====================================================` \  
`# Yaml` \  
`#====================================================` \  
apt-get install -y --no-install-recommends libyaml-dev && \  
pecl install yaml-2.0.0 && \  
docker-php-ext-enable yaml && \  
`#====================================================` \  
`# Blackfire` \  
`#====================================================` \  
curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$PHP_VERSION && \  
tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp && \  
mv /tmp/blackfire-*.so $(php -r "echo ini_get('extension_dir');")/blackfire.so
&& \  
printf "extension=blackfire.so\nblackfire.agent_socket=tcp://0.0.0.0:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini && \  
`#====================================================` \  
`# Composer` \  
`#====================================================` \  
apt-get install -y --no-install-recommends git && \  
php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');"
&& \  
php /tmp/composer-setup.php --filename=composer --install-dir=/usr/local/bin/
&& \  
chmod +x /usr/local/bin/composer && \  
rm /tmp/composer-setup.php && \  
`#====================================================` \  
`# PHPUnit` \  
`#====================================================` \  
curl -o /tmp/phpunit.phar https://phar.phpunit.de/phpunit.phar && \  
mv /tmp/phpunit.phar /usr/local/bin/phpunit && \  
chmod +x /usr/local/bin/phpunit && \  
`#====================================================` \  
`# Cleanup` \  
`#====================================================` \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ./overlay/ /  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
HEALTHCHECK --interval=5s --retries=3 --timeout=5s CMD \  
SCRIPT_NAME=/fpm-ping \  
SCRIPT_FILENAME=/fpm-ping \  
REQUEST_METHOD=GET \  
cgi-fcgi -bind -connect 127.0.0.1:9000 \  
| grep -q pong || exit 1  
  
WORKDIR /var/www/app  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["php-fpm"]  

