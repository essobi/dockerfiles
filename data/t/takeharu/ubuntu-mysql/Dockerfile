#Dockerfile  
FROM ubuntu:14.04  
MAINTAINER Takeharu Yamaguchi <https://github.com/takeharu>  
  
#setup  
RUN echo "mysql-server-5.5 mysql-server/root_password password root" |
debconf-set-selections  
RUN echo "mysql-server-5.5 mysql-server/root_password_again password root" |
debconf-set-selections  
RUN apt-get update && apt-get install -y mysql-server  
  
#enable access  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
CMD ["mysqld_safe"]  

