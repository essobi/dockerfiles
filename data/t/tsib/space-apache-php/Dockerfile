FROM tutum/apache-php  
RUN usermod -u 1000 www-data  
RUN apt-get update  
RUN apt-get install -y php5-xdebug  
RUN apt-get install -y sendmail  
RUN apt-get install -y vim  
RUN a2enmod expires && \  
a2enmod headers && \  
php5enmod mcrypt  
RUN apt-get install -y php5-imagick  
RUN service apache2 restart  
ADD hosts.sh /home/hosts.sh  

