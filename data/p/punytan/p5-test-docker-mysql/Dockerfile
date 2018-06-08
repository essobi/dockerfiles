FROM ubuntu:trusty  
  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates main
restricted" >> /etc/apt/sources.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ trusty-updates main
restricted" >> /etc/apt/sources.list  
RUN apt-get update  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
  
RUN apt-get install -y mysql-common  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y mysql-server  
  
RUN sed -i -e 's/127.0.0.1/0.0.0.0/' /etc/mysql/my.cnf  
  
RUN /etc/init.d/mysql restart && mysql -u root -h localhost --port 3306 -e
"grant all privileges on *.* to root@'%';"  
  
EXPOSE 3306  
RUN cat /etc/mysql/my.cnf  
  
CMD ["/usr/bin/mysqld_safe"]  

