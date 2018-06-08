FROM pelso/php-dev:7.2  
  
RUN apt update \  
&& apt install -y \  
php7.2-xdebug  
  
COPY xdebug.ini /etc/php/7.2/mods-available/xdebug.ini  
  
CMD service php7.2-fpm start \  
&& service php7.2-fpm restart \  
&& sleep infinity

