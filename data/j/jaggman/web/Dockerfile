FROM jaggman/php  
  
RUN apt-get update && \  
apt-get install -y nginx mysql-client && \  
mkdir -p /var/www/html/web  
  
ADD service.sh /etc/my_init.d/service.sh  
ADD www.conf /etc/php/7.2/fpm/pool.d/www.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD index.php /var/www/html/web/index.php  
RUN chmod a+x /etc/my_init.d/service.sh  
  
EXPOSE 80 443

