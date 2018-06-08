FROM macromind/docker-apache-php55  
MAINTAINER MACROMIND Online <idc@macromind.online>  
LABEL description="Zend Framework 1.12"  
  
RUN apt-get update && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/*  
ADD conf/000-docker.conf /etc/apache2/sites-available/  
RUN /usr/sbin/a2dissite '*' && /usr/sbin/a2ensite 000-docker  
  
EXPOSE 80  
WORKDIR /var/www/html/  
  
CMD ["apache2-foreground"]  

