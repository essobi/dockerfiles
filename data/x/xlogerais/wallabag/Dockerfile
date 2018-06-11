#  
# Dockerfile for Wallabag  
#  
# VERSION 1  
FROM debian:wheezy  
  
MAINTAINER Xavier Logerais <xavier@logerais.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# Update apt database  
RUN apt-get update  
  
# Install some utilities  
RUN apt-get install -y curl wget unzip ca-certificates  
  
# Install apache  
RUN apt-get install -y apache2  
  
# Install php  
RUN apt-get install -y php5 php5-curl php5-tidy php5-sqlite  
  
# Install Wallabag  
RUN wget http://wllbg.org/latest -O /tmp/wallabag-latest.zip && unzip -d
/var/www /tmp/wallabag-latest.zip && rm -rfv /tmp/wallabag-latest.zip  
RUN mv /var/www/wallabag-* /var/www/wallabag  
  
# Install Composer  
RUN cd /var/www/wallabag && curl -s http://getcomposer.org/installer | php &&
php composer.phar install  
  
# Fix perms  
RUN chown -R www-data /var/www/wallabag  
RUN chgrp -R www-data /var/www/wallabag  
  
VOLUME /var/log/apache2  
  
EXPOSE 80  
WORKDIR /var/www  
  
ENTRYPOINT ["/usr/sbin/apache2"]  
CMD ["-D", "FOREGROUND"]  

