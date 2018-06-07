FROM phusion/baseimage  
  
RUN apt-get update && \  
apt-get install -y wget software-properties-common && \  
LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \  
echo 'deb http://www.rabbitmq.com/debian/ testing main' | tee
/etc/apt/sources.list.d/rabbitmq.list && \  
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key
add \- && \  
mkdir -p /var/www/html/web && \  
mkdir -p /var/www/html/runtime/logs && \  
apt-get update && \  
apt-get install -y php php-fpm php-amqp php-mysql php-gd php-curl php-mbstring
php-xml php-intl php-zip php-pgsql php-memcached php-imagick php-sqlite3 \  
zip git rabbitmq-server supervisor nginx mysql-client && \  
wget -O- https://getcomposer.org/installer | php -- --install-dir=bin
--filename=composer && \  
composer global require "fxp/composer-asset-plugin:~1.1.1" && \  
ln -sf /var/www/html/runtime/logs/ /var/log/  
  
WORKDIR /var/www/html  
  
ADD service.sh /etc/my_init.d/service.sh  
ADD www.conf /etc/php/7.1/fpm/pool.d/www.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 80 443  
  
VOLUME [ "/var/www/html" ]  

