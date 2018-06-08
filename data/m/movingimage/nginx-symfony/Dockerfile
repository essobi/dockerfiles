FROM nginx:1.12  
MAINTAINER Daniel Louvier <daniel.louvier@movingimage.com>  
  
# Environment variables that can be influenced  
# from build parameters  
ONBUILD ARG HOSTNAME=example.com  
ONBUILD ARG NGINX_WEB_ROOT=/var/www  
ONBUILD ARG SYMFONY_WEB_ROOT=/var/www/web  
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
RUN mkdir -p $NGINX_WEB_ROOT/assets /var/blank  
# ONBUILD COPY ./assets $NGINX_WEB_ROOT/assets  
# Configuration files  
ONBUILD COPY ./nginx.conf /etc/nginx/nginx.conf  
ONBUILD COPY ./conf.d /etc/nginx/conf.d  
  
# Use 'sed' to template the hostfile. Because we use '/' in variables,  
# we have to use a different delimeter for sed. I chose '@'.  
ONBUILD RUN sed \  
-e "s@{{ symfony_web_root }}@$SYMFONY_WEB_ROOT@g" \  
-e "s@{{ php_fpm_host }}@$PHP_FPM_HOST@g" \  
-e "s@{{ nginx_web_root }}@$NGINX_WEB_ROOT@g" \  
-e "s@{{ symfony_env }}@$SYMFONY_ENV@g" \  
-e "s@{{ symfony_debug }}@$SYMFONY_DEBUG@g" \  
-e "s@{{ symfony_entrypoint }}@$SYMFONY_ENTRYPOINT@g" \  
-e "s@{{ symfony_entrypoint_escaped }}@$SYMFONY_ENTRYPOINT_ESCAPED@g" \  
/etc/nginx/conf.d/nginx_conf.conf.template > /etc/nginx/conf.d/$HOSTNAME.conf  
  
# Delete the configuration template and default configuration  
ONBUILD RUN rm /etc/nginx/conf.d/nginx_conf.conf.template
/etc/nginx/conf.d/default.conf  

