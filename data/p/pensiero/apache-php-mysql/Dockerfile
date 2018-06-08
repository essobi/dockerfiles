FROM pensiero/apache-php:php7.0  
# Labels  
LABEL maintainer "oscar.fanelli@gmail.com"  
  
# Mysql packages  
RUN apt update -q && apt install -yqq --force-yes \  
php-mysql  
  
# Start apache  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

