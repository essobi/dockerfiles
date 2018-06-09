FROM ubuntu:12.04  
MAINTAINER cpswan  
  
# install mysql  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server curl  
  
# listen on all interfaces, not only localhost  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
# open up access and create ToDoMVC database  
ADD ./startmysql.sh /opt/  
ADD ./todomvc.sql /tmp/  
  
# listen on standard MySQL port  
EXPOSE 3306  
# run MySQL  
CMD /bin/bash /opt/startmysql.sh  
  
# example usage:  
# sudo docker run -d -p 3306:3306 -name todomvc_db -v
/data/mysql:/var/lib/mysql cpswan/todomvc.mysql  

