FROM centos  
MAINTAINER Jon Dell  
ADD MariaDB.repo /etc/yum.repos.d/MariaDB.repo  
RUN yum install -y MariaDB-server  
VOLUME ["/var/lib/mysql"]  
EXPOSE 3306  
CMD ["/usr/bin/mysqld_safe"]  

