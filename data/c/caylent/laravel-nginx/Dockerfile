From richarvey/nginx-php-fpm:latest  
  
Maintainer Stefan Thorpe stefan@caylent.com  
  
ENV NGINX_SITE_HOME /var/www/html/  
ENV WEBROOT ${NGINX_SITE_HOME}/public  
  
# presetup composer to avoid cache misses  
COPY composer.* ${NGINX_SITE_HOME}/  
RUN composer install -n -d ${NGINX_SITE_HOME} \--no-dev --no-scripts --no-
autoloader  
  
# Add support for laravel scheduling  
RUN echo "* * * * * www-data /usr/share/nginx/html/artisan schedule:run >>
/dev/null 2>&1" >> /etc/conf.d/laravel && \  
echo "" >> /etc/conf.d/laravel  
  
# setup laravel  
ADD . ${NGINX_SITE_HOME}/  
RUN find ${NGINX_SITE_HOME}/ -type d -exec chmod 755 {} + && \  
find ${NGINX_SITE_HOME}/ -type d -exec chmod ug+s {} + && \  
find ${NGINX_SITE_HOME}/ -type f -exec chmod 644 {} + && \  
chown -R www-data:www-data ${NGINX_SITE_HOME}/ && \  
chmod -R 774 ${NGINX_SITE_HOME}/storage ${NGINX_SITE_HOME}/bootstrap/cache/ &&
\  
chmod +x ${NGINX_SITE_HOME}/artisan  
RUN composer dump-autoload -n -d ${NGINX_SITE_HOME} \--optimize  

