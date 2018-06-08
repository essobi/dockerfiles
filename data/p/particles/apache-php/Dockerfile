FROM debian  
MAINTAINER Fabio Ferrari <fabio@particles.io>  
  
RUN apt-get update && apt-get -y install apache2 php5 libapache2-mod-php5
php5-mcrypt && apt-get clean  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# vHost server settings  
RUN mkdir /etc/apache2/vhosts && \  
echo "IncludeOptional vhosts/*.conf" >> /etc/apache2/apache2.conf && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Enable mod_rewrite  
RUN /usr/sbin/a2enmod rewrite  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

