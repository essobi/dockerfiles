FROM phusion/baseimage:0.9.19  
RUN apt-get update\  
&& apt-get install -y wget php php-curl php-imagick php-gd php-mysql php-zip
php-mbstring php-fpm php-xml git locales sudo nginx supervisor  
  
RUN mkdir -p /var/www/html \  
&& chown -R www-data /var/www/html \  
&& chown -R www-data /var/lib/nginx \  
&& mkdir -p /var/www/.composer \  
&& chown -R www-data /var/www/.composer \  
&& gpasswd -a www-data sudo \  
&& echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
WORKDIR /var/www/html  
RUN rm index.nginx-debian.html \  
&& git clone https://github.com/movim/movim.git . \  
&& cp config/db.example.inc.php config/db.inc.php \  
&& wget -qO- https://getcomposer.org/installer | php \  
&& php composer.phar install \  
&& chown -R www-data /var/www/html  
  
VOLUME ["/var/www/html/log/","/var/www/html/users/","/var/www/html/cache/"]  
  
RUN sed -i 's/user\s*nginx;/user www-data;/' /etc/nginx/nginx.conf \  
&& rm /etc/php/7.0/fpm/pool.d/*  
COPY php-fpm-movim.conf /etc/php/7.0/fpm/pool.d/php-fpm-movim.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY configure-script /configure-script  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD supervisord -c /etc/supervisor/conf.d/supervisord.conf  
  

