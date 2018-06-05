FROM ubuntu:14.04.3  
RUN apt-get update && apt-get install -y nginx postgresql postgresql-contrib
php5-fpm  
  
COPY conf/php.ini /etc/php5/fpm/php.ini  
COPY conf/www.conf /etc/php5/fpm/pool.d/www.conf  
COPY conf/default /etc/nginx/sites-available/default  
COPY conf/info.php /usr/share/nginx/html/info.php  
COPY src/monit /usr/local/bin/monit  
COPY conf/monitrc /etc/monitrc  
RUN chmod 0700 /etc/monitrc  
CMD monit -I  

