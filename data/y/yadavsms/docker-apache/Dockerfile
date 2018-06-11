#Build image of ubuntu  
FROM ubuntu:latest  
  
MAINTAINER Somesh Yadav<somesh.yadav@imaginea.com>  
  
#update repo  
RUN apt-get -y update  
  
#install apache and php  
RUN apt-get -y install apache2  
RUN apt-get -y install php5 libapache2-mod-php5 php5-mcrypt  
RUN apt-get -y install libapache2-mod-auth-mysql php5-mysql php5  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /run/apache2/apache2.pid  
  
ADD wordpress.conf /etc/apache2/sites-available/  
  
RUN a2dissite 000-default  
  
RUN a2ensite wordpress  
  
#expose port 80  
EXPOSE 80  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

