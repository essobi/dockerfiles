FROM ubuntu:latest  
#Update Ubuntu  
RUN apt-get update  
#install nginx, php-fpm  
RUN apt-get install -y nginx php-fpm php-mysql php-gd php-bcmath php-zip php-
xml php-curl php-intl php-memcached php-xdebug  
#defining the environment  
ENV nginx_vhost /etc/nginx/sites-available/default  
ENV php_conf /etc/php/7.0/fpm/php.ini  
ENV nginx_conf /etc/nginx/nginx.conf  
  
#Enabling php-fpm on nginx server  
COPY default ${nginx_vhost}  
#Copying php.ini file to the server  
COPY php.ini ${php_conf}  
#Creating a new directory and changing owner  
RUN mkdir -p /run/php && chown -R www-data:www-data /var/www/html && chown -R
www-data:www-data /run/php  
  
#Volume configuration to let host machine access directories  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
  
#default container CMD and opening ports for http https, creating start.sh  
COPY start.sh /start.sh  
RUN chmod a+x start.sh  
CMD ["./start.sh"]  
EXPOSE 80 443  
  

