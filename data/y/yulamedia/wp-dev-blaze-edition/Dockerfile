FROM wordpress:php7.1-apache  
  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends less libxml2-dev \  
&& docker-php-ext-install soap \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add PHP Zip Archive extension  
RUN apt-get install -y zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install zip  
  
# Install Xdebug  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& rm -rf /tmp/pear/  
  
# Create Xdebug configuration  
RUN { \  
echo ''; \  
echo 'xdebug.remote_enable=on'; \  
echo 'xdebug.remote_autostart=on'; \  
echo 'xdebug.remote_connect_back=off'; \  
echo 'xdebug.remote_handler=dbgp'; \  
echo 'xdebug.profiler_enable=0'; \  
echo 'xdebug.profiler_output_dir="/var/www/html"'; \  
echo 'xdebug.remote_port=9000'; \  
} >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
RUN a2enmod rewrite expires  
  
VOLUME /var/www/html  
  
# Install WP CLI  
RUN curl -sSL -o /usr/local/bin/wp "https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar" \  
&& chmod +x /usr/local/bin/wp \  
&& mkdir -p /etc/wp-cli \  
&& chown www-data:www-data /etc/wp-cli  
  
RUN { \  
echo 'path: /var/www/html'; \  
echo 'url: localhost'; \  
echo 'apache_modules:'; \  
echo ' - mod_rewrite'; \  
} > /etc/wp-cli/config.yml  
  
RUN echo "export WP_CLI_CONFIG_PATH=/etc/wp-cli/config.yml" >
/etc/profile.d/wp-cli.sh  
  
COPY docker-entrypoint.sh /usr/local/bin/  

