FROM nitra/apache-symfony  
  
COPY . ./  
RUN rm -rf /var/www/app/cache/* /var/www/app/logs/*  
RUN mkdir -p web/bundles/framework  
RUN composer install -n  
RUN app/console assetic:dump && app/console assets:install  
RUN chown -R www-data. /var/www/app/cache /var/www/app/logs  
COPY docker/vhost.conf /etc/apache2/sites-enabled/000-default.conf  
COPY docker/php.ini /usr/local/etc/php  

