# Creates the backend for Supper  
FROM postgres:9.3.5  
MAINTAINER Ryan Baldwin <ryanbaldwin@gmail.com>  
  
ADD ./fix-acl.sh /docker-entrypoint-initdb.d/  
ADD ./setup_supper.sh /docker-entrypoint-initdb.d/  
#RUN chmod +x /docker-entrypoint-initdb.d/setup_supper.sh  

