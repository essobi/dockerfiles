FROM php:7.1-apache  
  
RUN a2enmod rewrite expires  
  
# install the PHP extensions we need  
RUN apt-get update && \  
apt-get install -y git libpng12-dev libjpeg-dev mysql-client && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \  
docker-php-ext-install gd mysqli opcache  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
#https://github.com/docker-library/wordpress/blob/master/fpm/Dockerfile  
ENV WORDPRESS_VERSION 4.7.5  
ENV WORDPRESS_SHA1 fbe0ee1d9010265be200fe50b86f341587187302  
  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
RUN curl -o wordpress.tar.gz -SL
https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz \  
&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz -C /usr/src/ \  
&& rm wordpress.tar.gz \  
&& rm -rf /var/www/html \  
&& mv /usr/src/wordpress /var/www/html \  
&& chown -R www-data:www-data /var/www/html  
  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar /usr/local/bin/wp  
  
RUN echo "alias wp='wp --allow-root'" >> ~/.bashrc  
  
ADD .htaccess /var/www/html/.htaccess  
ADD setup /setup  
  
ENTRYPOINT ["/setup"]  
CMD ["apache2-foreground"]  

