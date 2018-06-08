## based on mysql/mysql-server  
## https://github.com/mysql/mysql-docker/blob/mysql-server/8.0/Dockerfile  
FROM oraclelinux:7-slim  
  
ENV MYSQL_MAJOR 7.6  
ENV MYSQL_VERSION 7.6.4  
RUN set -x \  
\  
&& yum install -y https://dev.mysql.com/get/Downloads/MySQL-
Cluster-$MYSQL_MAJOR/mysql-cluster-community-server-
minimal-$MYSQL_VERSION-1.el7.x86_64.rpm \  
&& yum clean all \  
&& rm -rf \  
/var/tmp/* \  
/var/cache/yum/* \  
/var/run/mysqld/* \  
&& mkdir -p /var/lib/mysql-cluster /etc/mysql  
  
COPY my.cnf /etc/my.cnf  
COPY mysqld-entrypoint /  
COPY ndbd-entrypoint /  
COPY ndb_mgmd-entrypoint /  
COPY seeder /  

