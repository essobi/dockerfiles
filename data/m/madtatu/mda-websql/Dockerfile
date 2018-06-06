FROM ubuntu:14.04.3  
ENV DEBIAN_FRONTEND noninteractive  
  
# install packages  
RUN apt-get update ;\  
apt-get -y upgrade ;\  
apt-get -y install wget apache2 apache2-utils php5 php5-mysql php5-curl unzip;  
  
# Enable apache modules  
RUN a2enmod rewrite  
  
# add site  
ADD etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
available/000-default.conf  
  
# install mywebsql  
RUN wget
http://downloads.sourceforge.net/project/mywebsql/stable/mywebsql-3.6.zip  
  
RUN unzip mywebsql-3.6.zip -d /var/www  
  
# add htaccess  
ADD var/www/.htaccess /var/www/.htaccess  
  
# add mywebsql config  
ADD var/www/mywebsql/config/servers.php /var/www/mywebsql/config/servers.php  
  
ENV DEBIAN_FRONTEND dialog  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_DIR /var/run  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apache2ctl"]  
CMD ["-D", "FOREGROUND"]

