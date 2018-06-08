FROM ubuntu:12.04  
MAINTAINER Oliver Letterer <oliver.letterer@sparrow-labs.de>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y mysql-server-5.5 pwgen && apt-get clean  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# Add MySQL configuration  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
  
# Add MySQL scripts  
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh  
ADD import_sql.sh /import_sql.sh  
ADD create_db.sh /create_db.sh  
ADD create_slave.sh /create_slave.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Exposed ENV  
ENV MYSQL_USER admin  
ENV MYSQL_PASS **Random**  
ENV MYSQL_DATABASE icuisine  
  
ENV MYSQL_SERVER_ID 1  
# ENV MYSQL_MASTER_HOST master  
ENV MYSQL_REPLICATION_USER replication  
ENV MYSQL_REPLICATION_PASS **Random**  
  
# Add VOLUMEs to allow backup of config and databases  
# VOLUME ["/data", "/var/lib/mysql"]  
EXPOSE 3306  
CMD ["/run.sh"]  

