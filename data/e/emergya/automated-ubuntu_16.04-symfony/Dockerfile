FROM emergya/ubuntu_16.04-apache-php-mysql:201705191145-8d1948b  
  
ENV BUILD_TIMESTAMP 201704240142  
  
# Install symfony app dependencies with composer  
ADD assets/var/www/html /assets/var/www/html  
RUN /bin/bash -c 'if [ -e /assets/var/www/html/composer.json ]; then \  
mv /var/www/html /var/www/html.dist; \  
ln -s /assets/var/www/html /var/www/html; \  
mv /etc/php/7.0/cli/conf.d/20-xdebug.ini /tmp/; \  
composer install; \  
mv /tmp/20-xdebug.ini /etc/php/7.0/cli/conf.d/20-xdebug.ini; \  
chown -R www-data: /var/www/html/; \  
rm -f /var/www/html; mkdir /var/www/html; \  
else \  
exit 0; \  
fi'  
  
ADD assets /assets  
  
ENTRYPOINT ["/assets/bin/entrypoint-symfony"]  

