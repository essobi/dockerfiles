FROM ubuntu:trusty  
  
MAINTAINER Giacomo Triggiano <gtriggiano@treedom.net>  
  
# Add MySQL configuration  
COPY conf/my.cnf /etc/mysql/conf.d/my.cnf  
COPY conf/mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
  
RUN apt-get update && \  
apt-get -yq install \  
mysql-server-5.6 \  
rsyslog \  
curl \  
openssl \  
pwgen && \  
rm -rf /var/lib/apt/lists/* && \  
rm /etc/mysql/conf.d/mysqld_safe_syslog.cnf && \  
if [ ! -f /usr/share/mysql/my-default.cnf ] ; then cp /etc/mysql/my.cnf
/usr/share/mysql/my-default.cnf; fi && \  
mysql_install_db > /dev/null 2>&1 && \  
touch /var/lib/mysql/.EMPTY_DB  
  
# Add scripts  
COPY /scripts /  
  
RUN chmod 755 /*.sh  
  
ENV MYSQL_USER=admin \  
MYSQL_PASS=**Random** \  
ON_CREATE_DB=**False** \  
REPLICATION_MASTER=**False** \  
REPLICATION_SLAVE=**False** \  
REPLICATION_USER=replica \  
REPLICATION_PASS=replica  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
EXPOSE 3306  
CMD ["/run.sh"]  

