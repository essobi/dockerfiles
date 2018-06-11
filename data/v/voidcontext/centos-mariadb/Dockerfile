FROM centos  
  
ADD MariaDB.repo /etc/yum.repos.d/MariaDB.repo  
  
RUN yum upgrade -y  
RUN yum install -y MariaDB-server  
  
ADD my.cnf /etc/my.cnf  
  
ADD run.sh /opt/run.sh  
RUN chmod 744 /opt/run.sh  
  
CMD ["/opt/run.sh"]  

