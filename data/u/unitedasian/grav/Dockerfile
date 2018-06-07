FROM tgbyte/nginx-php-fpm  
  
MAINTAINER Olivier Pichon <op@united-asian.com>  
  
RUN usermod -u 1000 www-data  
  
RUN apt-get update && apt-get install -y \  
php5-curl \  
php5-gd  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
COPY . /usr/share/nginx/html  
  
RUN chown -R www-data:www-data /usr/share/nginx/html && \  
chmod -R 775 /usr/share/nginx/html && \  
chmod -R +s /usr/share/nginx/html && \  
umask 0002  
  
CMD ["/entrypoint.sh"]  

