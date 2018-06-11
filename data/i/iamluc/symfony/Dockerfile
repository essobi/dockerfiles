FROM php:7.0-apache  
  
# Extensions PHP  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
libicu-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install pdo_mysql intl  
  
# Blackfire  
#RUN export VERSION=`php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;"` \  
# && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/${VERSION} \  
# && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
# && mv /tmp/blackfire-*.so `php -r "echo
ini_get('extension_dir');"`/blackfire.so \  
# && echo "extension=blackfire.so\nblackfire.agent_socket=\${BLACKFIRE_PORT}"
> $PHP_INI_DIR/conf.d/blackfire.ini  
# Composer  
RUN curl -o /usr/local/bin/composer https://getcomposer.org/composer.phar &&
chmod +x /usr/local/bin/composer  
  
# Conf apache  
RUN a2enmod rewrite  
COPY vhost.conf /etc/apache2/sites-enabled/000-default.conf  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
WORKDIR /var/www/html  
  
EXPOSE 80  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["apache2-foreground"]  

