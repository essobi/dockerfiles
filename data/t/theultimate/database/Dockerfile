FROM mariadb  
MAINTAINER Maikel Dollé <maikel@itmagix.nl>  
  
RUN apt-get -y update && apt-get -y upgrade  
  
ENV MYSQL_RANDOM_ROOT_PASSWORD=yes  
ENV MYSQL_DATABASE=spotweb  
ENV MYSQL_USER=spotweb  
ENV MYSQL_PASSWORD=bewtops  
  
ADD spotwebinit.sql /docker-entrypoint-initdb.d  

