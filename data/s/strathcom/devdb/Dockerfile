FROM mysql:5.6  
ADD import /usr/local/bin/import  
ADD connect /usr/local/bin/connect  
  
# This replaces where the default entry point sets up mysql data.  
# It puts the mysql data files in a non-volume location so data can be  
# committed to the image  
RUN mkdir /var/lib/mysql_committed  
RUN sed -i 's/\/var\/lib\/mysql/\/var\/lib\/mysql_committed/g' /entrypoint.sh  
CMD ["mysqld", "--datadir=/var/lib/mysql_committed", "--user=mysql", "--
innodb-buffer-pool-size=32000000"]  

