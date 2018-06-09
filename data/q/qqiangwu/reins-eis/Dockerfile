FROM alpine:3.3  
MAINTAINER wuqq wqzhiep@gmail.com  
  
# install dependencies  
RUN apk update &&\  
apk add --no-cache mysql mysql-client &&\  
apk add --no-cache redis &&\  
apk add --no-cache openjdk7-jre &&\  
rm -f /var/cache/apk/* &&\  
mysql_install_db --user=root &> /dev/null &&\  
mkdir -p /run/mysqld  
  
ENV TERM dumb  
  
# install tomcat  
RUN wget -O tomcat.tar.gz
http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.68/bin/apache-
tomcat-7.0.68.tar.gz &&\  
gunzip tomcat.tar.gz &&\  
tar -xvf tomcat.tar && \  
mv apache-tomcat-7.0.68 /usr/local/tomcat && \  
rm -rf tomcat.tar.gz tomcat.tar  
  
# config mysql  
COPY my.cnf /etc/mysql/my.cnf  
  
ADD start.sh .  
RUN chmod +x start.sh  
  
ENTRYPOINT ["./start.sh"]  

