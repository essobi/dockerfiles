FROM ubuntu:14.04  
  
RUN apt-get -y update && \  
# Apache.  
apt-get -y install apache2 software-properties-common && \  
a2enmod proxy proxy_fcgi proxy_http rewrite ssl && \  
# Make www-data user uid/gid 1000 since this is the uid that boot2docker  
# will use for mounted directories.  
usermod -u 1000 www-data && \  
groupmod -g 1000 www-data && \  
# Install certbot for letsencrypt ssl cert management.  
add-apt-repository ppa:certbot/certbot && \  
apt-get -y update && \  
apt-get -y install python-certbot-apache  
  
# Configuration files.  
ADD default.conf /etc/apache2/sites-available/000-default.conf  
ADD entrypoint.sh /entrypoint.sh  
  
ENV PHP_DOCROOT /var/www/html  
ENV PHP_PORT 9000  
  
# Entry points.  
RUN chmod u+x /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
  
EXPOSE 80  

