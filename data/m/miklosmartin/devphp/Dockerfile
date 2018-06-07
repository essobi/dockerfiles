FROM nginx:latest  
  
MAINTAINER Martin Miklós <miklos.martin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# nginx conf tweak  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -e 's/user\s*nginx/user www-data/g' -i /etc/nginx/nginx.conf  
  
# install php  
RUN apt-get update && apt-get upgrade -y && apt-get install -y --fix-missing
php5-cli php5-fpm \  
php5-curl php5-gd php5-geoip php5-imagick php5-imap php5-intl \  
php5-mcrypt php5-memcache php5-memcached php5-redis \  
php5-mysql php5-pgsql php5-sqlite php5-apcu php5-xdebug  
  
# and composer  
RUN wget -O- https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/bin  
  
# forward fpm logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/php5-fpm.log  
  
# require and enable custom ini settings on builds  
ONBUILD ADD custom.php.ini /etc/php5/mods-available/custom.ini  
ONBUILD RUN ln -s /etc/php5/mods-available/custom.ini
/etc/php5/conf.d/99-custom.ini  
  

