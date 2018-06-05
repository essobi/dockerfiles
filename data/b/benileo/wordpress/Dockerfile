FROM php:5.6-apache  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache  
  
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
  
RUN a2enmod rewrite expires  
  
# increase upload file size to 64  
RUN { \  
echo 'upload_max_filesize=64M'; \  
echo 'post_max_size=64M'; \  
} > /usr/local/etc/php/conf.d/upload-size.ini  
  
ENV WORDPRESS_VERSION 4.6.1  
ENV WORDPRESS_SHA1 027e065d30a64720624a7404a1820e6c6fff1202  
  
RUN set -x \  
&& curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz" \  
&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz \  
&& cp -r wordpress/* . \  
&& rm -Rf wordpress \  
&& rm wordpress.tar.gz \  
&& chown -R www-data:www-data .  
  
RUN { \  
echo '<IfModule mod_rewrite.c>'; \  
echo 'RewriteEngine On'; \  
echo 'RewriteBase /'; \  
echo 'RewriteRule ^index\\.php$ - [L]'; \  
echo 'RewriteCond %{REQUEST_FILENAME} !-f'; \  
echo 'RewriteCond %{REQUEST_FILENAME} !-d'; \  
echo 'RewriteRule . /index.php [L]'; \  
echo '</IfModule>'; \  
} > .htaccess  
  
RUN chown www-data:www-data .htaccess  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
  
# ENTRYPOINT resets CMD  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

