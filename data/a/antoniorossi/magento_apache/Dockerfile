FROM debian:wheezy  
MAINTAINER antoniorossi <antoniorossi@outlook.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y install apache2 supervisor python && apt-get
clean  
RUN a2enmod rewrite  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_LOCK_DIR=/var/lock/apache2  
ENV APACHE_RUN_DIR=/var/run/apache2  
  
RUN mkdir /var/www/magento  
RUN mkdir /var/run/apache2/  
RUN chown -R $APACHE_RUN_USER:$APACHE_RUN_GROUP /var/www/magento  
RUN mv /var/www/index.html /var/www/magento  
COPY apache_supervisor.conf /etc/supervisor/conf.d/apache_supervisor.conf  
COPY apache2.conf /etc/apache2/  
  
VOLUME ["/var/log/apache2"]  
  
ADD ./default.conf /etc/apache2/sites-available/default  
  
EXPOSE 80  
CMD ["sh","-c","/usr/bin/supervisord"]  

