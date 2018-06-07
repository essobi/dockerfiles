FROM gregory90/php-wordpress:5.6  
RUN apt-get update && apt-get install -y ssh sudo git  
ADD php.ini /etc/php5/fpm/php.ini  
ADD php.ini /etc/php5/cli/php.ini  
  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  

