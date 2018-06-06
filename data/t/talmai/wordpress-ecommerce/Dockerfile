# Pull base image  
FROM wordpress:4.7-php7.1-apache  
  
# enable mod_rewrite  
RUN a2enmod rewrite  
  
# Install sudo in container in order to run wp-cli as the www-data user  
RUN apt-get update && \  
apt-get install -y sudo less && \  
apt-get install -y libpng12-dev libjpeg-dev libxml2-dev && \  
apt-get install -y libxslt-dev libgraphicsmagick1-dev graphicsmagick && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \  
docker-php-ext-install gd json mysqli pdo pdo_mysql opcache gettext exif
calendar && \  
docker-php-ext-install soap xsl sockets wddx  
  
# install APCu from PECL  
RUN pecl install apcu && docker-php-ext-enable apcu  
  
# install GMagick from PECL  
RUN pecl install gmagick-beta && docker-php-ext-enable gmagick  
  
COPY rootfs /  
RUN mv /wp-themes-setup.sh /bin/wp-themes-setup && chmod +x /bin/wp-themes-
setup  
  
# Add WP-CLI  
RUN curl -o /bin/wp-cli.phar https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar  
RUN mv /bin/wp-cli.phar /bin/wp  
RUN chmod +x /bin/wp  
  
# increase upload size  
# see http://php.net/manual/en/ini.core.php  
RUN { \  
echo "upload_max_filesize = 25M"; \  
echo "post_max_size = 50M"; \  
} > /usr/local/etc/php/conf.d/uploads.ini  
  
# Cleanup  
RUN rm -rf /tmp/* /var/tmp/*  

