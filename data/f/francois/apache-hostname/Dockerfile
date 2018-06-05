FROM debian:stretch  
MAINTAINER Francois Billant <fbillant@gmail.com>  
  
EXPOSE 80  
RUN apt-get update && \  
apt-get -y install apache2 libapache2-mod-php7.0 php7.0 \--no-install-
recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/run/apache2 && mkdir -p /var/log/apache2 && mkdir -p
/var/lock/apache2  
  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
  
RUN rm -f /var/www/html/index.html  
  
ADD index.php /var/www/html/index.php  
  
CMD [ "/usr/sbin/apache2", "-D", "FOREGROUND" ]  

