FROM centos:latest  
MAINTAINER dayreiner  
  
ENV MARIADB_MAJOR=10.1  
# MariaDB Repo  
COPY config/MariaDB.repo /etc/yum.repos.d/MariaDB.repo  
  
# Install required packages and MariaDB Vendor Repo  
RUN yum -y update && yum clean all && \  
rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB && \  
yum -y install http://www.percona.com/downloads/percona-
release/redhat/0.1-3/percona-release-0.1-3.noarch.rpm && \  
yum -y install MariaDB-server MariaDB-client galera percona-xtrabackup-24 less
which socat && yum clean all && \  
mkdir /docker-entrypoint-initdb.d  
  
RUN rm -rf /var/lib/mysql && mkdir /var/lib/mysql  
  
COPY config/server.cnf /etc/my.cnf.d/server.cnf  
COPY scripts/docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 3306  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["mysqld"]  

