FROM php:5.6.21-apache  
  
MAINTAINER kizi "stanislav.vojir@gmail.com"  
  
WORKDIR /var/www/html  
  
ENV term=xterm  
  
RUN apt-get update && \  
apt-get install -y pwgen git php5-curl php5-xsl php5-mysql mcrypt php5-mcrypt
libmcrypt-dev libxslt-dev libcurl4-openssl-dev zziplib-bin zlib1g-dev && \  
docker-php-ext-install -j$(nproc) curl xsl mysql mcrypt zip pdo pdo_mysql
sockets mysqli && \  
a2enmod headers && \  
a2enmod rewrite && \  
a2enmod proxy_http  
  
#repository files  
ADD / /var/www/html/easyminercenter  
RUN rm -rf /var/www/html/easyminercenter/docker  
  
#easyminercenter directory permissions  
RUN chmod -R 777 easyminercenter/log && \  
chmod -R 777 easyminercenter/temp && \  
chmod 777 easyminercenter/www/images/users && \  
touch easyminercenter/app/config/config.local.neon && \  
chmod 666 easyminercenter/app/config/config.local.neon  
  
#server configuration  
ADD docker/easyminer.conf /etc/apache2/sites-enabled  
ADD docker/proxy.conf /etc/apache2/mods-enabled  
ADD docker/db.php /root  
ADD docker/start.sh /root  
  
WORKDIR easyminercenter  
  
RUN php -r "readfile('https://getcomposer.org/installer');" | php && \  
php composer.phar update && \  
chmod 775 /root/start.sh && \  
mkdir temp/pmmlImports/cloud && \  
chmod 777 temp/pmmlImports/cloud  
  
ADD docker/config.local.neon /var/www/html/easyminercenter/app/config  
  
EXPOSE 80  
  
CMD ["/root/start.sh"]

