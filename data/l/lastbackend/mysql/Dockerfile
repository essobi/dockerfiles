FROM ubuntu:trusty  
MAINTAINER support@lastbackend.com  
  
# Add MySQL configuration  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
  
RUN apt-get update && \  
apt-get -yq install mysql-server-5.6 pwgen && \  
rm -rf /var/lib/apt/lists/* && \  
rm /etc/mysql/conf.d/mysqld_safe_syslog.cnf && \  
if [ ! -f /usr/share/mysql/my-default.cnf ] ; then cp /etc/mysql/my.cnf
/usr/share/mysql/my-default.cnf; fi && \  
mysql_install_db > /dev/null 2>&1 && \  
touch /var/lib/mysql/.EMPTY_DB  
  
# Add MySQL scripts  
ADD import_sql.sh /import_sql.sh  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
# Replication ENV  
ENV REPLICATION_MASTER **False**  
ENV REPLICATION_SLAVE **False**  
ENV REPLICATION_USER replica  
ENV REPLICATION_PASS replica  
  
# Add VOLUMEs to allow backup of config and databases  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
EXPOSE 3306  
CMD ["/init.sh"]

