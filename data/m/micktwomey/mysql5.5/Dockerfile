FROM ubuntu:14.04  
MAINTAINER mick@twomeylee.name  
  
RUN apt-get update && \  
apt-get install -y -q \  
mysql-server-5.5 \  
mysql-client-5.5 \  
libmysqlclient-dev \  
&& apt-get clean  
  
EXPOSE 3306  
  
RUN mkdir -p /mysql /mysql/etc /mysql/bin  
  
ADD mysql.sh /mysql/bin/mysql.sh  
ADD mysqld.cnf /mysql/etc/mysqld.cnf  
ADD my.cnf /mysql/etc/my.cnf  
  
RUN exec mysql_install_db \  
\--verbose \  
\--user=mysql \  
\--basedir=/usr \  
\--datadir=/mysql/data \  
\--defaults-file=/mysql/etc/mysqld.cnf  
  
RUN chown -R mysql /mysql  
  
RUN sudo -u mysql mysqld \--defaults-file=/mysql/etc/mysqld.cnf & \  
sleep 10 && \  
mysqladmin \--socket=/mysql/mysql.sock create docker && \  
echo "GRANT ALL ON *.* TO docker@'%' IDENTIFIED BY 'docker' WITH GRANT OPTION;
FLUSH PRIVILEGES" | mysql \--defaults-file=/mysql/etc/mysqld.cnf
\--socket=/mysql/mysql.sock  
  
USER mysql  
  
VOLUME ["/mysql/log", "/mysql/data"]  
  
CMD []  
ENTRYPOINT ["/usr/sbin/mysqld", "--defaults-file=/mysql/etc/mysqld.cnf"]  

