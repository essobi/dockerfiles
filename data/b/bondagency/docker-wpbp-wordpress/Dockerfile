FROM wordpress:php7.2-fpm-alpine  
  
# Install additional tools.  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories && \  
apk --no-cache add shadow postfix mysql-client zip unzip php7-zip php7-sockets
php7-soap zlib-dev libxml2-dev && \  
docker-php-ext-install zip soap sockets  
  
# Download and install WP-CLI.  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar /usr/local/bin/wp  
  
# Custom php.ini for sendmail path.  
COPY ./config/php.ini /usr/local/etc/php/conf.d/php.ini  
  
# Add the custom wp-config.  
COPY ./config/wp-config.php /var/www/config/wp-config.php  
  
# Make changes to php-fpm confg.  
# Reference: https://guides.wp-bullet.com/adjusting-php-fpm-performance-low-
memory/  
RUN sed -i -e 's/^pm = dynamic/pm = ondemand/g' /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e 's/^pm.max_children = 5/pm.max_children = 10/g' /usr/local/etc/php-
fpm.d/www.conf && \  
sed -i -e 's/^;pm.max_requests = 500/pm.max_requests = 500/g'
/usr/local/etc/php-fpm.d/www.conf  
  
WORKDIR /var/www/html  
  
# Custom entrypoint to install WP & replace wp-config  
# As we replace the original entrypoint from wordpress Dockerfile  
# we need to run that also in our replacement to actually install  
# the wordpress and start the PHP.  
COPY ./entrypoint.sh /custom-entrypoint.sh  
RUN chmod +x /custom-entrypoint.sh  
  
ENTRYPOINT ["/custom-entrypoint.sh"]  
  
CMD ["php-fpm"]

