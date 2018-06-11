FROM debian:jessie  
MAINTAINER Logan Sevcik <lsdaniel01@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
#APT Packages update  
RUN apt update && \  
apt upgrade -yq && \  
apt install -yq nginx php5 php5-fpm php5-mcrypt php5-json php5-curl php5-mysql
mysql-server && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
#Change Settings and Link  
RUN sed -i 's/memory_limit = 128M/memory_limit = 256M/' /etc/php5/fpm/php.ini
&& \  
sed -i 's/error_log = php_errors.log/error_log = \/dev\/stderr/'
/etc/php5/fpm/php.ini && \  
sed -i "s/display_errors = Off/display_errors = On/" /etc/php5/fpm/php.ini &&
\  
sed -i "s/error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT &
~E_NOTICE/error_reporting = E_ALL/" /etc/php5/fpm/php.ini && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
#Finalize  
RUN mkdir -p /srv/ && chmod -R 777 /srv  
ADD start.sh /start.sh  
ADD sites.txt /sites.txt  
VOLUME ["/srv"]  
EXPOSE 80 443  
CMD ["sh", "/start.sh"]  

