FROM ubuntu:latest  
  
MAINTAINER loint  
  
# MongoDB Repository  
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
  
# System update  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# MySQL - Redis  
RUN apt-get -y install mysql-client-5.6 mysql-server-5.6 mongodb-org redis-
server curl wget  
  
# Enable remote access (default is localhost only, we change this  
# otherwise our database would not be reachable from outside the container)  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
RUN sed -i -e"s/^bind 127.0.0.1/bind 0.0.0.0/" /etc/redis/redis.conf  
RUN sed -i -e"s/^bind_ip\s*=\s*127.0.0.1/bind_ip = 0.0.0.0/" /etc/mongod.conf  
  
# MySQL Setting  
ENV mysql_user admin  
ENV mysql_password penlook123  
ENV mysql_database penlook  
ENV mysql_right WRITE  
  
# MongoDB  
RUN mkdir -p /data/db  
  
ADD ./service /service  
ADD ./data /data  
RUN chmod +x /service/*  
RUN /service/mysql.sh  
  
ADD ./penlook /usr/local/bin/penlook  
RUN chmod +x /usr/local/bin/penlook  
ADD ./service /usr/local/bin/service  
RUN chmod +x /usr/local/bin/service/*  
  
CMD ["/bin/bash"]

