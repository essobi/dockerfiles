#Dockerfile  
FROM takeharu/ubuntu-mysql:latest  
MAINTAINER Takeharu Yamaguchi <https://github.com/takeharu>  
  
WORKDIR /work  
ADD ./create_database.sql /work/  
  
RUN service mysql start && \  
mysql -u root -proot < /work/create_database.sql  
  
VOLUME /var/lib/mysql  

