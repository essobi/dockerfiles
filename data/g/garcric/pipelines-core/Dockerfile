FROM ubuntu:14.04  
RUN apt-get update  
  
RUN apt-get install -y software-properties-common  
RUN locale-gen en_US.UTF-8  
  
RUN LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php  
  
RUN apt-get update  
  
RUN apt-get install -y --fix-missing git zip mcrypt mysql-server-5.5 php7.0
php7.0-mbstring php7.0-cli php7.0-curl php7.0-fpm php7.0-intl php7.0-json
php7.0-mcrypt php7.0-mysql php-mongodb php-apc php7.0-gd php7.0-xml
php7.0-soap  
  
RUN mkdir -p /run/php/ && chown -R www-data:www-data /run/php  
  
COPY php.ini /etc/php/7.0/fpm/php.ini  
  
COPY composer-installer /tmp/composer-installer.php  
RUN chmod 755 /tmp/composer-installer.php  
RUN php /tmp/composer-installer.php --install-dir=/usr/local/bin
--filename=composer  
  
VOLUME /var/lib/mysql  
  
#COPY start.sh /start.sh  
#RUN chmod 777 /start.sh  
#CMD ["/start.sh"]  

