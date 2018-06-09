FROM ubuntu:latest  
MAINTAINER Toby Padilla <tobypadilla@gmail.com>  
  
# Hack for initctl not being available in Ubuntu  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -s /bin/true /sbin/initctl  
  
# Install MySQL  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y mysql-server  
RUN apt-get clean  
  
# Listen on all interfaces  
RUN sed -i -e 's/127.0.0.1/0.0.0.0/' /etc/mysql/my.cnf  
  
# Allow root from non localhost IPs  
RUN /usr/sbin/mysqld & sleep 10s && mysql --host=127.0.0.1 --user=root -e
"GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'; FLUSH PRIVILEGES;"  
  
EXPOSE 3306  
ENTRYPOINT ["/usr/sbin/mysqld"]

