FROM ubuntu  
MAINTAINER Sarfaraz Ali Khan <mrkhan1417@gmail.com>  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y apache2 php-mysql libapache2-mod-php7.0 php7.0-mcrypt
php7.0-gd php7.0-curl  
  
RUN sed -i "s|/var/www|/www|g" /etc/apache2/apache2.conf  
RUN sed -i "s|/var/www/html|/www|g" /etc/apache2/sites-
available/000-default.conf  
  
EXPOSE 80  
WORKDIR /www  
  
COPY start.sh /opt/  
RUN chmod +x /opt/start.sh  
CMD ["/opt/start.sh"]  

