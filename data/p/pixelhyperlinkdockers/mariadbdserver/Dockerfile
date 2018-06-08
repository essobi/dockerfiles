# PixelHyperlink MariaDB 10.2.6 Server Docker  
#  
# VERSION 1.1.0  
FROM pixelhyperlinkdockers/ubuntu:v1.8.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with mariadb service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.1.0"  
LABEL com.pixelhyperlink.docker.mariadbserver.version="1.1.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.mariadbserver.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.mariadbserver.version.is-production="true"  
  
# Install MariaDB  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8 && \  
add-apt-repository 'deb [arch=amd64,i386]
http://mirror.jmu.edu/pub/mariadb/repo/10.2/ubuntu xenial main' && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get --purge remove mysql-server && \  
apt-get -y install mariadb-server  
  
# Expose mysql.  
EXPOSE 3306  
RUN mkdir /tmp/mysql && \  
rm -rf /var/lib/mysql/*  
  
VOLUME ["/var/lib/mysql", "/var/log/mysql", "/tmp/mysql"]  
  
# Copy mysql config  
COPY ./my.cnf /etc/mysql/my.cnf  
  
# Copy debian config  
COPY ./debian.cnf /etc/mysql/debian.cnf  
  
# Copy start up scripts  
COPY ./mariadb_entrypoint.sh /opt/mariadb_entrypoint.sh  
  
# Copy db setup SQL  
COPY ./db_setup.sql /opt/db_setup.sql  
  
# Change permission on startup scripts  
RUN chmod 755 /opt/mariadb_entrypoint.sh  
  
ENTRYPOINT ["/opt/mariadb_entrypoint.sh"]  

