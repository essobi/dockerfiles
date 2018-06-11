FROM martinhelmich/typo3  
LABEL maintainer="Kris Raich"  
  
#import files  
COPY res/run.sh /root/run.sh  
COPY res/db.sql /tmp/db.sql  
COPY res/LocalConfiguration.php /var/www/html/typo3conf/LocalConfiguration.php  
  
RUN apt-get update  
RUN apt-get install -y git wget nano  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN apt-get install -y mysql-server  
RUN /etc/init.d/mysql start && mysql -u root < /tmp/db.sql  
RUN chown www-data:www-data /var/www/html/typo3conf/LocalConfiguration.php  
RUN rm -f /tmp/db.sql  
RUN apt-get clean  
  
CMD bash /root/run.sh  
  
#export DB  
#mysqldump -u root typo3 > export.html  

