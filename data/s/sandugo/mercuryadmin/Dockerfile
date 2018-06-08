FROM centurylink/apache-php:latest  
  
# install project & packages  
RUN apt-get update && apt-get -y install vim mysql-client  
RUN git clone https://eb8c41d26d90262dd4fa8e88176094b85f7f7269:x-oauth-
basic@github.com/131db/mercury.git /app  
  
# appconfig files  
COPY docker-files/database.php /app/application/config/database.php  
RUN cp /app/application/config/constants-sample.php
/app/application/config/constants.php  
RUN chmod 644 /app/application/config/database.php  
RUN chmod 644 /app/application/config/constants.php  
  
# database  
COPY docker-files/tables.sql /tables.sql  
COPY docker-files/sampledata.sql /sampledata.sql  
  
# fix permissions  
RUN chmod 777 /app/application/logs  
RUN chmod 777 /app/application/cache  
RUN chown -R www-data:www-data /app  
  
# mod run  
COPY docker-files/run.sh /run.sh  
RUN chmod 755 /run.sh  
  
EXPOSE 80 3306  
CMD ["/run.sh"]  

