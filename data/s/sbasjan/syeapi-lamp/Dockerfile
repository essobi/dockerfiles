FROM sbasjan/syeapi-lamp-base:latest  
  
#Based on https://github.com/mattrayner/docker-lamp  
#Based on https://github.com/dgraziotin/osx-docker-lamp  
MAINTAINER Marco Basile <marco.basile@netinsight.net>  
  
ENV MYSQL_ADMIN_PASS="123liveott"  
ENV MYSQL_USER_DB="SIMnet"  
ENV MYSQL_USER_NAME="sye"  
ENV MYSQL_USER_PASS="neti"  
COPY ./src/app/ /app  
RUN mkdir -p /sql  
ADD ./src/sql/ /sql  
ADD ./src/supporting_files/create_mysql_users.sh /create_mysql_users.sh  
  

