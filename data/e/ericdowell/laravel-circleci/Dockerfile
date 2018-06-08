FROM circleci/php:7.2-fpm-stretch-node-browsers  
  
## Upgrade all dependencies and global composer version and set defaults for
php and add needed nginx sources  
RUN sudo apt-get upgrade -y && sudo composer self-update \  
&& sudo mkdir -p /home/cirlceci/project && sudo chmod 770
/home/cirlceci/project \  
&& echo "date.timezone = UTC" | sudo tee /usr/local/etc/php/conf.d/date.ini \  
&& echo "memory_limit = -1" | sudo tee /usr/local/etc/php/conf.d/memory.ini \  
&& echo "deb http://nginx.org/packages/debian/ stretch nginx" | sudo tee
--append /etc/apt/sources.list \  
&& echo "deb-src http://nginx.org/packages/debian/ stretch nginx" | sudo tee
--append /etc/apt/sources.list  
  
## Add nginx GPG key  
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
ABF5BD827BD9BF62  
  
## Install nginx and supervisor  
RUN sudo apt-get update && sudo apt-get install -y nginx supervisor  
  
## Install node and php extensions  
RUN sudo apt-get install -y autoconf libicu-dev libxml2-dev libpng-dev
libjpeg-dev zlib1g-dev \  
mysql-client xvfb chromium \  
&& sudo docker-php-ext-configure intl \  
&& sudo docker-php-ext-install intl \  
&& sudo docker-php-ext-install zip \  
&& sudo docker-php-ext-install gd \  
&& sudo docker-php-ext-install soap \  
&& sudo docker-php-ext-install mysqli \  
&& sudo docker-php-ext-install pdo_mysql \  
&& sudo docker-php-ext-install sockets  
  
## Remove default nginx config  
RUN sudo rm /etc/nginx/conf.d/default.conf  
## Add default nginx config  
ADD conf/default.nginx.conf /etc/nginx/conf.d/default.conf  
  
## Add supervisord configs for nginx/php-fpm  
ADD conf/nginx.supervisord.conf /etc/supervisor/conf.d/nginx.conf  
ADD conf/php-fpm.supervisord.conf /etc/supervisor/conf.d/php-fpm.conf  
  
## Run autoremove  
RUN sudo apt-get --purge autoremove  
  
CMD sudo /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf  

