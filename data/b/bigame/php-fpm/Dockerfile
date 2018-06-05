FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR "/var/www/html"  
  
RUN apt-get update\  
&&mkdir -p /etc/php/7.0/mods-available\  
&&echo 'extension=amqp.so'>/etc/php/7.0/mods-available/amqp.ini\  
&&apt-get install -y --no-install-recommends php-fpm php-mcrypt php-xdebug
php-amqp php-mongodb php-redis php-mbstring php-gd php-imagick php-mysql php-
curl php-igbinary php-xml php-apcu libzookeeper-mt2 curl\  
&&apt-get install -y --no-install-recommends ca-certificates\  
&&rm -rf /var/lib/apt/lists/*  
  
COPY /ext/*.so /usr/lib/php/20151012/  
COPY /ext/*.ini /etc/php/7.0/mods-available/  
RUN phpenmod swoole yaf\  
&&phpdismod xdebug\  
&&mkdir /run/php  
COPY www.conf /etc/php/7.0/fpm/pool.d/  
COPY docker-entrypoint.sh /usr/bin/  
RUN chmod +x /usr/bin/docker-entrypoint.sh  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]  
CMD ["php-fpm7.0","--nodaemonize"]  

