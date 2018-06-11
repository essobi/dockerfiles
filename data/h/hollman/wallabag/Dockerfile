FROM ubuntu:latest  
MAINTAINER Hollman Enciso <hollman.enciso@gmail.com>  
RUN apt-get update && apt-get -y dist-upgrade  
  
#Install the neccesary packages  
RUN apt-get -y install apache2 php5 php5-gd php5-imap php5-mcrypt
php5-memcached php5-mysql mysql-client php5-curl php5-tidy php5-sqlite curl
git sqlite3  
  
#This will install the required dependency Twig via Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
#RUN cd /var/www/html/ && /usr/local/bin/composer install  
RUN rm -rf /var/www/html/*  
  
#cloning the project  
RUN git clone https://github.com/wallabag/wallabag.git /var/www/html/  
RUN chown -R www-data: /var/www/html/  
  
#setting the document root volume  
VOLUME ["/var/www/html/"]  
  
#Set some apache variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
#Expose default apache port  
EXPOSE 80  
#run apache on background  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

