FROM lysender/php7-apache  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
ADD ./start-apache2.sh /start-apache2.sh  
RUN chmod 755 /*.sh  
RUN mkdir -p /etc/supervisor/conf.d  
ADD ./supervisor-apache2.conf /etc/supervisor/conf.d/apache2.conf  
ADD apache-default.conf /etc/apache2/sites-available/000-default.conf  
  
# Mount the env vars from host  
VOLUME ["/var/www/html", "/var/log/apache2"]  
  
EXPOSE 80  
CMD ["supervisord", "-n"]  

