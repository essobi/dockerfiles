# Download base image ubuntu 16.04  
FROM ubuntu:16.04  
# Update Ubuntu Software repository and musql-server  
RUN apt-get update  
  
#I njection of admin password  
RUN ["/bin/bash", "-c", "debconf-set-selections <<< 'mysql-server mysql-
server/root_password password your_password'"]  
RUN ["/bin/bash", "-c", "debconf-set-selections <<< 'mysql-server mysql-
server/root_password_again password your_password'"]  
  
#installation of mysql server  
RUN apt-get install -y \  
mysql-server  
  
# Launch and enable mySql.exe  
# RUN service mysql start #Launch in init_db  
# Copy the database schema to the /data directory  
ADD files/run_db files/init_db files/db_schema.sql files/db_basisinfo.sql
/tmp/  
  
# init_db will create the default  
# database from db_schema.sql and db_basisinfo.sql, then  
# stop mysqld, and finally copy the /var/lib/mysql directory  
# to default_mysql_db.tar.gz  
# Modify mode to allow run_db and init_db to be execute  
RUN chmod u+x /tmp/init_db && chmod u+x /tmp/run_db  
  
# run_db starts mysqld, but first it checks  
# to see if the /var/lib/mysql directory is empty, if  
# it is it is seeded with default_mysql_db.tar.gz before  
# the mysql is fired up  
RUN /tmp/init_db  
  
EXPOSE 3306  
#To change configuration  
COPY files/mysqld.cnf /etc/mysql/mysql.conf.d/  
  
#We need to keep this  
ENTRYPOINT "/tmp/run_db"  

