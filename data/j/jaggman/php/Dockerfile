FROM phusion/baseimage  
  
RUN apt-get update && \  
apt-get install -y vim zip git wget software-properties-common && \  
LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get install -y php php-fpm php-odbc php-amqp php-mysql php-gd php-curl
php-mbstring php-xml \  
php-intl php-zip php-pgsql php-memcached php-imagick php-sqlite3 && \  
wget -O- https://getcomposer.org/installer | php \-- --install-dir=bin
--filename=composer  
  
WORKDIR /var/www/html  
VOLUME [ "/var/www/html" ]  

