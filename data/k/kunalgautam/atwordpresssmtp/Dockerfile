FROM php:5.6-apache  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libjpeg-dev \  
libpng-dev \  
sendmail sendmail-bin mailutils \  
unzip \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli  
# TODO consider removing the *-dev deps and only keeping the necessary lib*
packages  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN { \  
echo 'sendmail_path = /usr/sbin/sendmail -t -i'; \  
echo 'SMTP = localhost'; \  
echo 'smtp_port = 25'; \  
} > /usr/local/etc/php/conf.d/smtp.ini  
  
RUN a2enmod rewrite expires  
  
VOLUME /var/www/html  
  
ENV WORDPRESS_VERSION 4.9.6  
ENV WORDPRESS_SHA1 40616b40d120c97205e5852c03096115c2fca537  
  
RUN set -ex; \  
curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz"; \  
echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
tar -xzf wordpress.tar.gz -C /usr/src/; \  
rm wordpress.tar.gz; \  
chown -R www-data:www-data /usr/src/wordpress; \  
usermod -u 1000 www-data  
#usermod option to match with default user on Linux system for fixing file
permission issue  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

