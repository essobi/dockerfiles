from centos:7  
MAINTAINER Mattias Hemmingsson  
  
#  
#  
# This will start the first node and boostrap the cluster  
# You must always need ONE cluster node starting up  
#  
# docker run -i -t --name cluster_master mariadb-cluster-master  
#  
# Give it the name cluster_master so that the slave cluster can add to that
name  
LABEL name="Mariadb Cluster"  
LABEL vendor="Lifeandshell"  
  
RUN echo -e "[mariadb] \nname = MariaDB \nbaseurl =
http://yum.mariadb.org/10.1/centos7-amd64
\ngpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB \ngpgcheck=1 \n " >
/etc/yum.repos.d/MariaDB.repo  
  
RUN yum install MariaDB-server MariaDB-client -y  
RUN yum install which -y  
RUN mysql_install_db -u mysql  
  
ADD config/* /opt/install/  
RUN mysqld_safe & sleep 10 && mysql < /opt/install/init-sql.sql  
  
ADD config/server.cnf /etc/my.cnf.d/  
RUN chmod 644 /etc/my.cnf.d/server.cnf  
  
#Starting the mysql as mysql user and starting the cluster  
CMD su mysql -s/bin/bash -c "/usr/sbin/mysqld --basedir=/usr
--datadir=/var/lib/mysql --plugin-dir=/usr/lib64/mysql/plugin --user=mysql
--wsrep-new-cluster"

