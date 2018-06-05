FROM rafaeldiez/centos6-cacti  
MAINTAINER Rafael Diez  
  
RUN service mysqld start  
RUN service httpd start  
RUN echo "*/5 * * * * root php /var/www/html/cacti/poller.php > /dev/null
2>&1" >> /var/spool/cron/root  
EXPOSE 80  

