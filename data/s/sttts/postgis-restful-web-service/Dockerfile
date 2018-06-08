FROM ubuntu:14.04  
MAINTAINER Dr. Stefan Schimanski <stefan.schimanski@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y php5-fpm php5-pgsql python-psycopg2
unzip nginx curl supervisor python-pip  
RUN pip install supervisor-stdout  
  
ADD postgis.conf /etc/nginx/sites-enabled/postgis.conf  
RUN rm /etc/nginx/sites-enabled/default  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
RUN ln -sf /dev/stderr /var/log/php5-fpm.log  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN mkdir -p /var/postgis && cd /var/postgis && curl -f -orest.zip
'https://postgis-restful-web-service-framework.googlecode.com/files/restful-
framework-v1.1.zip' && unzip rest.zip && rm rest.zip  
ADD database.inc.php /var/postgis/rest/inc/database.inc.php  
  
ADD php-fpm-env.conf /etc/php5/fpm/pool.d/php-fpm-env.conf  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-n"]  
EXPOSE 80  

