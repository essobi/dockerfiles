FROM centos:centos7  
  
MAINTAINER Mikael Keto  
  
# add mariadb repository  
ADD mariadb.repo /etc/yum.repos.d/mariadb.repo  
  
# install mariadb  
RUN yum -y install MariaDB-server MariaDB-client && yum clean all && rm -rf
/var/cache/yum  
  
VOLUME ["/var/lib/mysql"]  
  
ENTRYPOINT ["mysqld"]

