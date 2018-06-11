FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php5 php5-mysql php5-gd php-pear php-apc php5-curl curl lynx-cur vim-tiny  
  
RUN apt-get install -y mysql-server  
  
RUN apt-get install -y supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisor.conf  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php5/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
RUN mkdir /workingdir  
# Copy site into place.  
ADD phpmyadmin /workingdir/www/phpmyadmin  
  
VOLUME /workingdir/  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
EXPOSE 80  
EXPOSE 3306  
# By default, simply start apache.  
#CMD /usr/sbin/apache2ctl -D FOREGROUND  
CMD ["/usr/bin/supervisord"]  

