# Image to build the container from. If you need an older PHP version  
# (i.e. 5.3) you'd use an older version of Ubuntu (ubuntu:12.04).  
FROM ubuntu:14.04  
MAINTAINER Leandro Di Tommaso <leandro.ditommaso@mikroways.net>  
  
# Packages to install on the container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
--force-yes \  
supervisor php5-fpm php5-gd php5-imagick php5-curl php5-mcrypt php5-json \  
php5-mysqlnd  
  
# Define environment variables.  
# Change the following to rename your app or change the user and group the app
will run  
# with. I don't recommend modifying the user and group but there's no problem
in changing  
# the app name.  
ENV APP_NAME www  
ENV APP_USER www-data  
ENV APP_GROUP www-data  
  
# Create directory for the application.  
RUN mkdir -p /opt/applications  
RUN mkdir -p /var/log/phpfpm && chown $APP_USER:$APP_GROUP /var/log/phpfpm  
RUN mkdir -p /var/run/phpfpm && chown $APP_USER:$APP_GROUP /var/run/phpfpm  
  
# php.ini customizations.  
RUN sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 10M/g"
/etc/php5/fpm/php.ini  
RUN sed -i "s/post_max_size = 8M/post_max_size = 10M/g" /etc/php5/fpm/php.ini  
  
# PHP-FPM pool configuration.  
RUN rm /etc/php5/fpm/pool.d/www.conf  
ADD www.conf /etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/pool_name/$APP_NAME/g" /etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/app_user/$APP_USER/g" /etc/php5/fpm/pool.d/www.conf  
RUN sed -i "s/app_group/$APP_GROUP/g" /etc/php5/fpm/pool.d/www.conf  
  
# Change the default error log location.  
RUN sed -i "s@error_log = /var/log/php5-fpm.log@error_log =
/var/log/phpfpm/php5-fpm.error.log@g" /etc/php5/fpm/php-fpm.conf  
  
# Add supervisord to make sure service restarts if something fails.  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf  

