FROM crashvb/supervisord:latest  
MAINTAINER Richard Davis <crashvb@gmail.com>  
  
# Install packages, download files ...  
RUN APT_ALL_REPOS=1 docker-apt apache2 libapache2-mod-fastcgi php-apcu
php7.0-cli php7.0-fpm  
  
# Configure: hello  
ADD hello.* /var/hello/  
RUN chown --recursive root:root /var/hello  
  
# Configure: httpd  
ADD default.apache2 /etc/apache2/sites-available/000-default.conf  
ADD php7-fpm.apache2 /etc/apache2/conf-available/php7-fpm.conf  
RUN a2enconf php7-fpm && \  
a2enmod actions cgid  
  
# Configure: php7.0-fpm  
RUN install --directory --group=www-data --mode=0755 --owner=www-data
/var/run/php  
  
# Configure: supervisor  
ADD supervisord.apache2.conf /etc/supervisor/conf.d/apache2.conf  
ADD supervisord.php.conf /etc/supervisor/conf.d/php.conf  
  
EXPOSE 80/tcp  

