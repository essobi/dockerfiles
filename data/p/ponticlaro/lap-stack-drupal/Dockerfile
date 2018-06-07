FROM ponticlaro/lap-stack  
  
MAINTAINER Cristiano Baptista "cristiano.baptista@ponticlaro.com"  
# Install S3FS  
ADD .docker/s3fs/install.sh /usr/bin/s3fs-install  
RUN chmod +x /usr/bin/s3fs-install  
RUN sh /usr/bin/s3fs-install  
  
# PHP-FPM: copy config files to container  
ADD .docker/php-fpm/config/php.drupal.ini /etc/php5/fpm/php.ini

