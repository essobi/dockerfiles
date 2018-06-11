FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y software-properties-common build-
essential wget curl  
  
RUN mkdir -p /var/www/html  
RUN mkdir -p /etc/docker  
  
# NGINX  
RUN add-apt-repository -y ppa:nginx/stable && apt-get update && apt-get
install -y nginx  
COPY docker/nginx /etc/nginx  
  
# PHP  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C
&& \  
add-apt-repository -y ppa:ondrej/php && \  
apt-get update && \  
apt-get install -y php7.0-cli php7.0-fpm \  
php7.0-mysql php7.0-sqlite php7.0-curl php7.0-gd php7.0-gmp php7.0-mcrypt
php7.0-memcached \  
php7.0-imagick php7.0-intl php7.0-json php7.0-dev php7.0-zip php7.0-redis
php7.0-mbstring php-pear php-xdebug  
COPY docker/php /etc/php/7.0  
  
## Composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
# Supervisor  
RUN apt-get install -y supervisor  
  
COPY docker /etc/docker  
  
EXPOSE 80 443  
CMD /usr/bin/supervisord -c /etc/docker/supervisord.conf  

