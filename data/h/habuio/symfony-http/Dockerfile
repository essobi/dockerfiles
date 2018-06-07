FROM nginx:1.12  
MAINTAINER Ruben Knol <c.minor6@gmail.com>  
  
# Environment variables that can be influenced  
# from build parameters  
ONBUILD ARG HOSTNAME=example.com  
ONBUILD ARG NGINX_WEB_ROOT=/var/www  
# For production should be prod  
ONBUILD ARG SYMFONY_ENV=dev  
# For production should be - app.php -  
ONBUILD ARG SYMFONY_ENTRYPOINT="app_dev.php"  
# For production should be - app\\\\.php -  
ONBUILD ARG SYMFONY_ENTRYPOINT_ESCAPED="app_dev\\\\.php"  
# For production should be 0  
ONBUILD ARG SYMFONY_DEBUG=1  
ONBUILD ARG PHP_FPM_HOST=php-fpm  
  
# Asset files  
RUN mkdir -p $NGINX_WEB_ROOT/assets  
ONBUILD COPY ./web/assets $NGINX_WEB_ROOT/assets  
ONBUILD COPY ./web/robots.txt $NGINX_WEB_ROOT/robots.txt  
ONBUILD COPY ./web/favicon.ico $NGINX_WEB_ROOT/favicon.ico  
  
# Configuration files  
COPY ./nginx.conf /etc/nginx/nginx.conf  
COPY ./conf.d /etc/nginx/conf.d  
  
# Use 'sed' to template the hostfile. Because we use '/' in variables,  
# we have to use a different delimeter for sed. I chose '@'.  
ONBUILD RUN sed \  
-e "s@{{ php_fpm_host }}@$PHP_FPM_HOST@g" \  
-e "s@{{ nginx_web_root }}@$NGINX_WEB_ROOT@g" \  
-e "s@{{ symfony_env }}@$SYMFONY_ENV@g" \  
-e "s@{{ symfony_debug }}@$SYMFONY_DEBUG@g" \  
-e "s@{{ symfony_entrypoint }}@$SYMFONY_ENTRYPOINT@g" \  
-e "s@{{ symfony_entrypoint_escaped }}@$SYMFONY_ENTRYPOINT_ESCAPED@g" \  
/etc/nginx/conf.d/symfony_php_no_ssl.conf.template >
/etc/nginx/conf.d/$HOSTNAME.conf  
  
# Delete the configuration template and default configuration  
ONBUILD RUN rm /etc/nginx/conf.d/symfony_php_no_ssl.conf.template
/etc/nginx/conf.d/default.conf  

