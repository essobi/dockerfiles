FROM php:5.6.22-apache  
MAINTAINER Michaël Rivet <rivet.michael@gmail.com>  
  
# Installs php extensions  
RUN apt-get update && apt-get install -y \  
git \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
mysql-client \  
libcurl3 \  
libcurl3-dev \  
libxml2-dev  
RUN docker-php-ext-install mcrypt gd curl pdo_mysql mbstring mysqli soap  
  
# Blackfire probe  
RUN curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/56 \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so `php -r "echo
ini_get('extension_dir');"`/blackfire.so \  
&& echo "extension=blackfire.so\nblackfire.agent_socket=\${BLACKFIRE_PORT}" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Custom PHP ini configuration  
COPY ./z-php.ini /usr/local/etc/php/conf.d/  
  
# Default document root  
ENV APACHE_DOC_ROOT=/srv/  
# Silent composer message  
ENV COMPOSER_DISABLE_XDEBUG_WARN=1  
# Activating mod rewrite & headers  
RUN a2enmod rewrite  
RUN a2enmod headers  
  
# Add www-data to root group and viceversa  
RUN usermod -u 1000 www-data  
  
# change ownership of www-data root directory  
RUN chown -R www-data:www-data /var/www  
RUN su - www-data -s /bin/bash -c "composer global require symfony/var-dumper"  
  
# Default index.php for testing  
COPY public/index.php /srv/  
  
# Volume for Apache root directory  
VOLUME /srv  
WORKDIR /srv  
  
# Start!  
COPY ./run.sh /  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  

