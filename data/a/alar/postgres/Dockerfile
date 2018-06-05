# Version 0.0.1  
FROM postgres:9.5  
MAINTAINER Alar Software LLC <dev@alarllc.com>  
  
ENV DB_NAME database  
ENV DB_USER admin  
ENV DB_PASS password  
ENV DB_SUPERUSER false  
  
ADD setup-remote-connections.sh /docker-entrypoint-initdb.d/setup-remote-
connections.sh  
RUN chmod 755 /docker-entrypoint-initdb.d/setup-remote-connections.sh  
ADD setup-database.sh /docker-entrypoint-initdb.d/  
RUN chmod 755 /docker-entrypoint-initdb.d/setup-database.sh  

