FROM ubuntu:14.04.2  
MAINTAINER khiraiwa  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /data_apache2/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME localhost  
ENV APACHE_SERVERALIAS docker.localhost  
ENV APACHE_DOCUMENTROOT /data_apache2/www  
  
# Initialize apt-get  
RUN ["apt-get", "update"]  
ENV DEBIAN_FRONTEND noninteractive  
RUN ["apt-get", "install", "apache2", "libapache2-mod-php5", "php5-cli", "php-
apc", "php5-mcrypt", "mysql-client-5.6", "php5-mysql", "php5-curl", "openssl",
"libapache2-mod-rpaf", "-y"]  
RUN ["a2enmod", "php5"]  
RUN ["a2enmod", "ssl"]  
RUN ["a2enmod", "rewrite"]  
RUN ["a2enmod", "rpaf"]  
  
# Mount data dir  
RUN ["mkdir", "-p", "/data_apache2/log/apache2"]  
RUN ["mkdir", "-p", "/data_apache2/www"]  
  
# Add ssl conf file  
ADD 001-default-ssl.conf /etc/apache2/sites-available/001-default-ssl.conf  
ADD 000-default.conf /etc/apache2/sites-available/000-default.conf  
RUN ["ln", "-s", "/etc/apache2/sites-available/001-default-ssl.conf",
"/etc/apache2/sites-enabled/001-default-ssl.conf"]  
RUN ["rm", "-f", "/etc/apache2/sites-enabled/000-default.conf"]  
RUN ["ln", "-s", "/etc/apache2/sites-available/000-default.conf",
"/etc/apache2/sites-enabled/000-default.conf"]  
ADD ports.conf /etc/apache2/ports.conf  
ADD php.ini /etc/php5/apache2/php.ini  
  
# Set DocumentRoot Dir  
RUN ["rm", "-rf", "/var/www/html"]  
RUN ["ln", "-s", "/data_apache2/www", "/var/www/html"]  
  
RUN ["chown", "-R", "www-data:www-data", "/etc/apache2"]  
RUN ["chown", "-R", "www-data:www-data", "/data_apache2"]  
  
VOLUME ["/data_apache2"]  
  
EXPOSE 443  
EXPOSE 1111  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

