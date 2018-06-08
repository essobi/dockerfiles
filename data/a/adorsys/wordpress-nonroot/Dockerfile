FROM php:7.1-apache  
  
RUN echo "Listen 8080" > /etc/apache2/ports.conf && \  
sed -i /VirtualHost/s/80/8080/ /etc/apache2/sites-available/000-default.conf  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libjpeg-dev \  
libpng12-dev \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli opcache  
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
  
#upload  
RUN { \  
echo "file_uploads = On\n"; \  
echo "upload_max_filesize = 25M\n"; \  
echo "post_max_size = 25M\n"; \  
echo "max_execution_time = 600\n"; \  
} > /usr/local/etc/php/conf.d/uploads.ini  
  
RUN a2enmod rewrite expires  
  
RUN mkdir -p /var/www/html; \  
chmod -R 777 /var/www/html  
  
VOLUME /var/www/html  
  
ENV WORDPRESS_VERSION 4.7.1  
ENV WORDPRESS_SHA1 8e56ba56c10a3f245c616b13e46bd996f63793d6  
  
RUN set -ex; \  
curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz"; \  
echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
tar -xzf wordpress.tar.gz -C /usr/src/; \  
rm wordpress.tar.gz;  
  
RUN chmod -R 777 /usr/src/wordpress /var/lock/apache2 /var/run/apache2  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 8080  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

