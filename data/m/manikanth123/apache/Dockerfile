FROM ubuntu:14.04  
MAINTAINER d.basivireddy@gmail.com  
RUN apt-get update && apt-get install -y apache2 supervisor  
RUN apt-get install -y php5 php5-mysql php5-memcached php5-gd  
ADD websites /var/www/html/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  
  

