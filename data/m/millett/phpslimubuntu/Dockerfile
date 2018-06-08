FROM ubuntu:14.04  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install apache2 -y  
RUN apt-get install php5 libapache2-mod-php5 php5-mcrypt -y  
RUN a2enmod rewrite  
  
COPY apache/apache2.conf /etc/apache2/  
  
RUN service apache2 restart  
  
WORKDIR /var/www/html  
  
COPY app/ /var/www/html  
  
RUN chmod -R 777 /var/www/html  
  
RUN service apache2 restart  
  
EXPOSE 80  
  
# By default, simply start apache.  
CMD /usr/sbin/apache2ctl -D FOREGROUND

