FROM mysql:5.6  
  
MAINTAINER Edmondo Porcu<edmondo.porcu@instapartners.it>  
  
USER root  
  
COPY *.sql /docker-entrypoint-initdb.d/  
  
ENV MYSQL_ROOT_PASSWORD=camunda-test

