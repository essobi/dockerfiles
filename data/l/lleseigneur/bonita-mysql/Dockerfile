FROM mysql:5.5.49  
MAINTAINER Laurent Leseigneur <laurent.leseigneur@bonitasoft.com>  
  
ENV MYSQL_ROOT_PASSWORD=root  
  
# set docker.cnf config  
COPY docker.cnf /etc/mysql/conf.d  
  
COPY init-databases.sql /docker-entrypoint-initdb.d  

