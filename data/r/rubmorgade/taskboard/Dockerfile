############################################################  
# Dockerfile to run a Django-based web application  
# Based on an Ubuntu Image  
############################################################  
# Set the base image to use to Ubuntu  
FROM ubuntu:14.04  
# Set the file maintainer (your name - the file's author)  
MAINTAINER Ruben Morgade  
  
# Update the default application repository sources list  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y apache2 php5 libapache2-mod-php5 sqlite3 php5-common
php5-cgi php5-sqlite php-config  
  
RUN sudo a2enmod rewrite && sudo a2enmod expires  
  
EXPOSE 80  
ADD TaskBoard.tar.gz /var/www/html  
RUN chmod -R 755 /var/www/html && chown -R www-data:www-data /var/www/html &&
sed -i 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
ENTRYPOINT ["docker-entrypoint.sh"]  
  

