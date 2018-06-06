# Dockerfile of Apache CloudStack mgmt. server MySQL DB on Ubuntu  
  
FROM ubuntu:14.04  
  
MAINTAINER opsforge.io  
LABEL name="cloudstack-mysql"  
LABEL version="0.2.0"  
  
CMD service mysql restart && tail -f /var/log/mysql/error.log  
  
ENV mysqlpass 'Standard1'  
  
USER root  
  
EXPOSE 3306  
  
VOLUME ["/var/lib/mysql"]  
  
RUN apt-get update && \  
export DEBIAN_FRONTEND="noninteractive" && \  
echo "mysql-server mysql-server/root_password password $mysqlpass" | debconf-
set-selections && \  
echo "mysql-server mysql-server/root_password_again password $mysqlpass" |
debconf-set-selections && \  
apt-get install mysql-server -y && \  
apt-get clean all  
  
RUN sed -i -e 's/\(user.*\)/user\t\t= root/g' /etc/mysql/my.cnf && \  
sed -i -e 's/\(\# \* InnoDB.*\)/\# \*
InnoDB\ninnodb_rollback_on_timeout=1\ninnodb_lock_wait_timeout=600\n/g'
/etc/mysql/my.cnf && \  
sed -i -e 's/\(bind-address.*\)/bind-address\t\t= 0.0.0.0/g' /etc/mysql/my.cnf
&& \  
sed -i -e 's/\(\#max_connections.*\)/max_connections\t\t= 700/g'
/etc/mysql/my.cnf && \  
sed -i -e 's/\(\#log_bin.*\)/log_bin\t\t\t= \/var\/log\/mysql\/mysql-
bin.log/g' /etc/mysql/my.cnf && \  
sed -i -e 's/\(\max_binlog_size.*\)/max_binlog_size\t= 100M\nbinlog-format =
'\''ROW'\''/g' /etc/mysql/my.cnf  

