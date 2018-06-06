# build on top of the latest LTS  
FROM ubuntu:trusty  
MAINTAINER You "salih-emin@ubuntu.com"  
# Update the package list info  
RUN apt-get -y update  
  
# Install the dependencies  
RUN apt-get install -y apache2 php5 php5-gd php-xml-parser php5-intl
php5-sqlite smbclient curl libcurl3 php5-curl bzip2 wget  
  
# Get the latest Owncloud and extract it to the web server folder  
RUN wget -O - https://download.owncloud.org/community/owncloud-8.2.1.tar.bz2 |
tar jx -C /var/www/  
  
# Give the permissions to apache  
RUN chown -R www-data:www-data /var/www/owncloud  
  
# Enable the site  
ADD ./001-owncloud.conf /etc/apache2/sites-available/  
RUN ln -s /etc/apache2/sites-available/001-owncloud.conf /etc/apache2/sites-
enabled/  
RUN a2enmod rewrite  
  
# Tell Docker to NAT port 80 on the host to the container when it’s run  
EXPOSE :80  
# Start Apache’s httpd in the foreground is so that Docker can manage the
process  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

