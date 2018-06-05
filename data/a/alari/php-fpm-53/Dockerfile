FROM ubuntu:precise  
  
MAINTAINER Dmitry Kurinskiy <name.alari@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install php-pear php5-cgi php5-cli php5-common php5-curl
php5-fpm php5-gd php5-imagick php5-intl php5-mcrypt php5-mysql php5-tidy
php5-xsl  
  
RUN sed -i '/^listen/c \  
listen = 0.0.0.0:9000' /etc/php5/fpm/pool.d/www.conf  
  
RUN sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php5/fpm/php-fpm.conf  
  
RUN mkdir /srv/http  
RUN echo "<?php phpinfo(); ?>" > /srv/http/index.php  
  
EXPOSE 9000  
VOLUME /srv/http  
  
VOLUME /tmp  
  
CMD ["/usr/sbin/php5-fpm"]  

