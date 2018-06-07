FROM debian:wheezy  
  
MAINTAINER Thierry Piaf <thierry@piaf.eu>  
  
RUN apt-get update && apt-get install -y curl git nginx php5-fpm php5-cli
php5-xdebug  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
COPY config/vhost.conf /etc/nginx/sites-enabled/default  
COPY entrypoint.sh /root/entrypoint.sh  
  
VOLUME ["/var/www", "/var/log/nginx/"]  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["/root/entrypoint.sh"]  

