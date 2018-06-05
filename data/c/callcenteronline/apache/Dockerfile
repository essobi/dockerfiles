FROM ubuntu  
RUN apt-get update && apt-get install -y apt-utils net-tools inetutils-ping
sudo  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
RUN apt-get install apache2 -y  
RUN a2enmod ssl  
RUN a2ensite default-ssl  
RUN update-rc.d apache2 enable  
  
ENV TERM xterm  
  
CMD service apache2 start && bash  

