FROM centos  
MAINTAINER kevin.mcgrath@sungardas.com  
  
ADD config/MariaDB.repo /etc/yum.repos.d/  
ADD config/galera.cnf /etc/my.cnf.d/galera.cnf  
RUN rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB  
RUN yum install -y which MariaDB-Galera-server MariaDB-client galera  
  
VOLUME ["/var/log", "/var/lib/mysql"]  
EXPOSE 3306 4567 4568 4444  
ENTRYPOINT ["mysqld"]  

