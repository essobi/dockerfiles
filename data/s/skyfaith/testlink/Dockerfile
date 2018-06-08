FROM ubuntu:15.10  
MAINTAINER skyfaith@tocpa.cn  
RUN apt-get update -yqq && \  
apt-get install -yqq vim apache2 php5 wget php5-mysql  
RUN wget -q
http://sourceforge.net/projects/testlink/files/TestLink%201.9/TestLink%201.9.9/testlink-1.9.9.tar.gz/download
-O testlink-1.9.9.tar.gz &&\  
tar zxvf testlink-1.9.9.tar.gz && \  
mv testlink-1.9.9 /var/www/html/testlink && \  
rm testlink-1.9.9.tar.gz  
RUN echo "max_execution_time=3000" >> /etc/php5/apache2/php.ini && \  
echo "session.gc_maxlifetime=60000" >> /etc/php5/apache2/php.ini  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
RUN mkdir -p /var/testlink/logs /var/testlink/upload_area  
ADD config_db.inc.php /var/www/html/testlink  
RUN sed -i 's/\/html/\/html\/testlink/g' /etc/apache2/sites-
enabled/000-default.conf  
RUN sed -i "s/config_check_warning_mode = 'FILE'/config_check_warning_mode =
'SILENT'/g" /var/www/html/testlink/config.inc.php  
RUN chmod 777 -R /var/www/html/testlink && \  
chmod 777 -R /var/testlink/logs && \  
chmod 777 -R /var/testlink/upload_area  
EXPOSE 80/tcp  
CMD ["/usr/sbin/apache2","-D", "FOREGROUND"]  

