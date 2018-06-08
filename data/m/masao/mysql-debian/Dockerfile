# docker build -t masao/mysql-ubuntu .  
# docker run --name mysql -d -e 'DB_NAME=dbname' masao/mysql-ubuntu:latest  
FROM debian:jessie  
MAINTAINER Masashi Okumura <masao@classcat.com>  
  
RUN apt-get update && apt-get install -y mysql-server  
  
RUN sed -i -e "s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
ADD cc-init /cc-init  
RUN chmod 755 /cc-init  
  
EXPOSE 3306  
CMD ["/cc-init"]  

