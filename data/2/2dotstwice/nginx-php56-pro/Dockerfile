FROM 2dotstwice/nginx-php56-starter  
  
MAINTAINER Kristof Coomans "kristof@2dotstwice.be"  
ENV REFRESHED_AT "2016-11-20 07:30:00"  
# Pro hosting package nginx configuration  
# Increase worker processes from 2 to 4.  
RUN sed -i -e "s/worker_processes 2/worker_processes 4/g"
/etc/nginx/nginx.conf  
  
# Pro hosting package php-fpm configuration  
ADD ./files/etc/php5/fpm/pool.d/www.conf /etc/php/5.6/fpm/pool.d/www.conf  

