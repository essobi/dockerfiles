FROM ubuntu:14.04.2  
MAINTAINER khiraiwa  
  
# Initialize apt-get  
RUN ["apt-get", "update"]  
ENV DEBIAN_FRONTEND noninteractive  
RUN ["apt-get", "install", "mysql-server-5.6", "-y"]  
  
RUN sed -i -e"s/bind-address = 127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
# Mount data dir  
RUN ["mkdir", "/data_mysql"]  
VOLUME ["/data_mysql"]  
  
EXPOSE 3306  
CMD ["/usr/bin/mysqld_safe"]  

