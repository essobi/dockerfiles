# PixelHyperlink Mysql 5.7 Server Docker  
#  
# VERSION 1.4.0  
FROM pixelhyperlinkdockers/ubuntu:v1.8.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with mysql service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.4.0"  
LABEL com.pixelhyperlink.docker.mysqlserver.version="1.4.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.mysqlserver.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.mysqlserver.version.is-production="true"  
  
# Install MySQL  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install mysql-server mysql-client  
  
# Expose apache.  
EXPOSE 3306  
RUN mkdir /tmp/mysql && \  
rm -rf /var/lib/mysql/*  
  
VOLUME ["/var/lib/mysql", "/var/log/mysql", "/tmp/mysql"]  
  
# Copy mysql config  
COPY ./mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf  
  
# Copy debian config  
COPY ./debian.cnf /etc/mysql/debian.cnf  
  
# Copy start up scripts  
COPY ./mysql_entrypoint.sh /opt/mysql_entrypoint.sh  
  
# Copy db setup SQL  
COPY ./db_setup.sql /opt/db_setup.sql  
  
# Change permission on startup scripts  
RUN chmod 755 /opt/mysql_entrypoint.sh  
  
ENTRYPOINT ["/opt/mysql_entrypoint.sh"]  

