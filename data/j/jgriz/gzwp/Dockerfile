FROM php:7.1-apache  
  
# Set permissions, install the PHP extensions, and create self-signed ssl cert  
RUN usermod -u 1000 www-data \  
&& groupmod -g 1000 www-data \  
&& chown -R -h 1000 /var/www/html \  
&& chgrp -R -h 1000 /var/www/html \  
&& apt-get update && apt-get install -y sudo less mysql-client openssl
libpng12-dev \  
libjpeg-dev && rm -rf /var/lib/apt/lists/* \  
&& curl -o /bin/wp-cli.phar https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli zip \  
&& a2enmod rewrite expires ssl \  
&& mkdir -p /etc/apache2/ssl \  
&& openssl req \  
-new \  
-newkey rsa:2048 \  
-days 365 \  
-nodes \  
-x509 \  
-subj "/C=US/ST=California/L=San Diego/O=Grizzly/OU=Development/CN=localhost" \  
-out /etc/apache2/ssl/server.crt \  
-keyout /etc/apache2/ssl/server.key  
  
# WordPress install vars  
# See https://wordpress.org/download/release-archive  
ENV WP_VERSION 4.7.2  
ENV WP_SHA1 7b687f1af589c337124e6247229af209ec1d52c3  
  
# Upstream tarballs include ./wordpress/ so this gives us
/var/www/html/wordpress  
RUN set -x \  
&& curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WP_VERSION}.tar.gz" \  
&& echo "$WP_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz -C /var/www/html/ \  
&& rm wordpress.tar.gz \  
&& mv /var/www/html/wordpress/* ./ \  
&& rm -rf /var/www/html/wordpress \  
&& rm /var/www/html/wp-config-sample.php  
  
# Copy scripts and files  
COPY wp-config.php /var/www/html/  
COPY .htaccess /var/www/html/  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY php.ini /usr/local/etc/php/  
COPY ssl.conf /etc/apache2/  
COPY wp-su.sh /bin/wp  
  
# Update permissions and apache configuration  
RUN chmod 640 /var/www/html/wp-config.php \  
&& cat /etc/apache2/ssl.conf >> /etc/apache2/apache2.conf \  
&& rm /etc/apache2/ssl.conf \  
&& chmod +x /bin/wp-cli.phar \  
&& chmod +x /bin/wp  
  
# ENTRYPOINT and CMD  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

