FROM debian  
MAINTAINER Daniel Atkinson <hourd.tasa@gmail.com>  
  
RUN apt-get update && apt-get install -y --fix-missing \  
aptitude \  
bash \  
nginx \  
php5-fpm \  
php5-json \  
php5-mysql \  
php5-mcrypt \  
php5-sqlite \  
php5-curl \  
php5-gd \  
php5-ldap \  
php5-ssh2 \  
libssh2-php \  
ssh \  
git \  
nodejs \  
supervisor  
  
RUN mkdir -p /etc/nginx/sites-enabled /var/run/php-fpm /var/log/supervisor  
  
RUN rm /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD .docker/nginx/sites-enabled/default /etc/nginx/sites-enabled/default  
ADD fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.conf  
  
VOLUME ["/var/www", "/etc/nginx/sites-enabled"]  
  
ADD nginx-supervisor.ini /etc/supervisor.d/nginx-supervisor.ini  
ADD .docker/php/php.ini /etc/php/php.ini  
  
EXPOSE 80 9000  
  
WORKDIR /var/www  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.d/nginx-supervisor.ini"]  

