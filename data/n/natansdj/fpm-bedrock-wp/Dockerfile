FROM php:7.0-fpm-alpine  
  
ENV DB_NAME=wordpress \  
DB_USER=root \  
DB_HOST=mariadb \  
DB_PASSWORD=root \  
WP_ENV=development  
  
# taken from Wordpress offical fpm Dockerfile, for the most part  
# https://github.com/docker-
library/wordpress/blob/7d40c4237f01892bb6dbc67d1a82f5b15f807ca1/php7.0/fpm/Dockerfile  
# install the PHP extensions we need  
RUN apk --update add less bash su-exec mysql-client freetype-dev libjpeg-
turbo-dev libpng-dev \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache  
  
# install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
# php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'aa96f26c2b67226a324c27919f1eb05f21c248b987e6195cad9690d5c1ff713d53020a02ac8c217dbf90a7eacc9d141d')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  
# install wordpress cli  
# https://github.com/KaiHofstetter/docker-wordpress-cli/blob/master/Dockerfile  
COPY wp.sh /usr/local/bin/wp  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && chmod +x /usr/local/bin/wp && \  
mv wp-cli.phar /usr/local/bin/wp-cli.phar  
  
# taken from Wordpress offical fpm Dockerfile  
# https://github.com/docker-
library/wordpress/blob/7d40c4237f01892bb6dbc67d1a82f5b15f807ca1/php7.0/fpm/Dockerfile  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# taken from mkz71's comment on Wordpress official Docker Hub page  
# https://hub.docker.com/_/wordpress/  
RUN { \  
echo 'file_uploads = On'; \  
echo 'memory_limit = 256M'; \  
echo 'upload_max_filesize = 256M'; \  
echo 'post_max_size = 300M'; \  
echo 'max_execution_time = 600'; \  
} > /usr/local/etc/php/conf.d/uploads.ini  
  
# set folder permissions  
RUN chown -R www-data:www-data . && chmod g+s .  
  
# install bedrock & set permissions  
RUN su-exec www-data composer create-project roots/bedrock . && chmod -R 755 .  
  
# install mcrypt  
RUN apk add libmcrypt-dev \  
&& docker-php-ext-install mcrypt mbstring  
  
# install xdebug  
RUN apk add build-base autoconf && \  
pecl install -o -f xdebug && \  
rm -rf /tmp/pear && \  
docker-php-ext-enable xdebug && \  
sed -i '1 a xdebug.remote_autostart=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini && \  
sed -i '1 a xdebug.remote_mode=req' /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini && \  
sed -i '1 a xdebug.remote_handler=dbgp' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini && \  
sed -i '1 a xdebug.remote_connect_back=0' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini && \  
sed -i '1 a xdebug.remote_port=9000' /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini && \  
sed -i '1 a xdebug.idekey=PHPSTORM' /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini && \  
sed -i '1 a xdebug.remote_host=172.18.0.1' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini && \  
sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini && \  
apk del build-base && \  
rm -rf /var/cache/apk/*  
  
# init script and CMD  
COPY init.sh /opt/  
RUN chmod +x /opt/init.sh  
CMD /opt/init.sh && exec php-fpm  

