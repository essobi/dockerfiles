FROM recesscreative/docker-wordpress:4.7.2  
ENV WP_ROOT /usr/src/wordpress  
  
COPY vhost.conf /etc/nginx/conf.d  
COPY 99-custom.ini /usr/local/etc/php/conf.d  
  
COPY wp-config.php $WP_ROOT  
RUN chown -R deployer:www-data $WP_ROOT \  
&& chmod 640 $WP_ROOT/wp-config.php

