FROM undownding/nginx-http2  
  
RUN apt-get update \  
&& apt-get install -y supervisor \  
php5-fpm php5-gd php5-mysql \  
php5-json php5-intl php5-curl \  
php5-xdebug php5-mcrypt php5-sqlite \  
php5-xmlrpc php5-xsl php5-geoip \  
php5-ldap php5-memcache php5-memcached \  
php5-imagick php5-redis php-pear php5-memcached \  
&& rm -rf /var/lib/apt/lists/* && apt-get clean  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN echo "<?php phpinfo(); ?>" > /usr/share/nginx/html/index.php \  
&& rm /usr/share/nginx/html/index.html \  
&& mkdir /php \  
&& sed -i "s/\/var\/run\/php5-fpm.sock/127.0.0.1:9000/g"
/etc/php5/fpm/pool.d/www.conf \  
&& rm -rf /var/log/nginx && mkdir /var/log/nginx  
  
CMD ["/usr/bin/supervisord"]  

