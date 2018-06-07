FROM greatfox/ssh  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
RUN apt-get -y install mysql-server  
  
RUN echo 'mysqld_safe& sleep 3; mysqladmin password MustChange; mysqladmin
shutdown -pMustChange; sleep 3' | /bin/sh  
  
RUN mv /etc/mysql/my.cnf /etc/mysql/my.cnf.backup  
RUN /bin/sed -e 's/127\\.0\\.0\\.1/0.0.0.0/' /etc/mysql/my.cnf.backup >
/etc/mysql/my.cnf  
  
RUN echo "/usr/bin/service mysql start" >> /initrc  
  

