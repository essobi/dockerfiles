FROM ubuntu:12.04  
MAINTAINER MACROMIND Online <idc@macromind.online>  
LABEL description="MACROMIND Online Dev - Ubuntu + Apache2 + PHP 5.3"  
  
RUN apt-get update && apt-get -y install git curl apache2 php5 php5-mysql
php5-mcrypt php5-json php5-imap libapache2-mod-php5 php5-curl php5-gd unzip &&
apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN chown www-data:www-data /usr/sbin/apachectl && chown www-data:www-data
/var/www/  
RUN a2enmod php5  
RUN a2enmod rewrite  
RUN a2ensite default-ssl  
RUN a2enmod ssl  
RUN chown www-data:www-data /usr/sbin/apache2ctl && rm -rf /var/www  
RUN echo "ServerName localhost" > /etc/apache2/conf.d/fqdn.conf  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
  
COPY apache2-foreground /usr/local/bin/  
  
EXPOSE 80  
EXPOSE 443  
WORKDIR /var/www/  
  
CMD ["apache2-foreground"]  

