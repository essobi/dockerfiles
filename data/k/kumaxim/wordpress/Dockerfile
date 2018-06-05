FROM php:5.6-apache  
  
MAINTAINER Kudryavtsev Maxim <kumaxim@users.noreply.github.com>  
  
# Require Apache module for Wordpress  
RUN a2enmod rewrite expires headers  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli  
  
ENV XDEBUG_VERSION 2.4.1  
ENV XDEBUG_SHA1 52b5cede5dcb815de469d671bfdc626aec8adee3  
  
# Install XDebug from source  
RUN set -xe \  
&& cd /usr/src \  
&& curl -fSL "https://xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz" -o
xdebug.tgz \  
&& echo "$XDEBUG_SHA1 xdebug.tgz" | sha1sum -c - \  
&& mkdir -p /usr/src/xdebug \  
&& tar -xzf xdebug.tgz -C /usr/src/xdebug --strip-components=1 \  
&& cd /usr/src/xdebug \  
&& phpize \  
&& ./configure --enable-xdebug \  
&& make -j"$(nproc)" \  
&& make -j"$(nproc)" install \  
&& { \  
echo 'zend_extension=xdebug.so'; \  
echo 'xdebug.remote_enable=1'; \  
echo 'xdebug.remote_autostart=1'; \  
echo 'xdebug.remote_port=9000'; \  
echo 'xdebug.remote_handler=dbgp'; \  
echo 'xdebug.remote_mode=req'; \  
echo 'xdebug.idekey=wp-debug'; \  
} | tee "/usr/local/etc/php/conf.d/xdebug.ini" \  
&& make -j"$(nproc)" clean \  
&& rm -rf /usr/src/xdebug  
  
EXPOSE 9000  
# Disable browser cache in current configuration file  
# See http://stackoverflow.com/questions/49547/making-sure-a-web-page-is-not-
cached-across-all-browsers  
RUN { \  
echo; \  
echo '<ifModule mod_headers.c>'; \  
echo '\tHeader unset ETag'; \  
echo '\tHeader set Cache-Control "max-age=0, no-cache, no-store, must-
revalidate"'; \  
echo '\tHeader set Pragma "no-cache"'; \  
echo '\tHeader set Expires "Wed, 11 Jan 1984 05:00:00 GMT"'; \  
echo '</ifModule>'; \  
} | tee --append "$APACHE_CONFDIR/conf-available/docker-php.conf"  
  
ENV WORDPRESS_VERSION 4.6.1  
ENV WORDPRESS_SHA1 027e065d30a64720624a7404a1820e6c6fff1202  
  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
RUN curl -fSL "https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz" -o
wordpress.tar.gz \  
&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz -C /usr/src \  
&& rm wordpress.tar.gz \  
&& { \  
# NOTE: The "Indexes" option is disabled in the base image  
echo '# BEGIN WordPress'; \  
echo '<IfModule mod_rewrite.c>'; \  
echo 'RewriteEngine On'; \  
echo 'RewriteBase /'; \  
echo 'RewriteRule ^index\\.php$ - [L]'; \  
echo 'RewriteCond %{REQUEST_FILENAME} !-f'; \  
echo 'RewriteCond %{REQUEST_FILENAME} !-d'; \  
echo 'RewriteRule . /index.php [L]'; \  
echo '</IfModule>'; \  
echo '# END WordPress'; \  
} | tee "/usr/src/wordpress/.htaccess" \  
&& chown -R www-data:www-data /usr/src/wordpress  
  
VOLUME /var/www/html  
  
# Setup wp-config.php and add xdebug.remote_host parameter  
COPY wordpress-entrypoint.sh /entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

