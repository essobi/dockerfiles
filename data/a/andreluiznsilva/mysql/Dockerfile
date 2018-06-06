# Mysql 5.7  
FROM mysql:5.7  
MAINTAINER Andre Nascimento <andreluiznsilva@gmail.com>  
  
ENV MYSQL_ROOT_PASSWORD="root"  
ENV MYSQL_DATABASE="default"  
ENV MYSQL_USER="mysql"  
ENV MYSQL_PASSWORD="mysql"  
ENV MYSQL_SCRIPT="SELECT 1 FROM DUAL;"  
RUN echo '#!/bin/bash \n echo "$MYSQL_SCRIPT" > /docker-entrypoint-
initdb.d/init.sql\n'"$(cat /usr/local/bin/docker-entrypoint.sh)" >
/usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 3306  
WORKDIR /usr/local/mysql  

