FROM pensiero/apache-php  
  
# Labels  
LABEL maintainer "oscar.fanelli@gmail.com"  
  
# Mysql packages  
RUN apt update -q && apt install -yqq --force-yes \  
php-mysql \  
php-mongodb  
  
# Start apache  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

