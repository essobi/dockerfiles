FROM centos:6.6  
RUN yum -y install mysql-server-5.1.73  
  
COPY my.cnf /etc/my.cnf  
COPY initial.sql /initial.sql  
  
RUN mysql_install_db  
  
USER mysql  
  
CMD ["mysqld_safe", "--init-file=/initial.sql", "--skip-name-resolve"]  
  
EXPOSE 3306  

