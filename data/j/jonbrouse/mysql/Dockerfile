FROM alpine:3.4  
RUN apk add --update mysql mysql-client && \  
rm -rf /var/cache/apk/*  
  
COPY assets/create_import_db.sh /tmp/create_import_db.sh  
  
RUN chmod +x /tmp/create_import_db.sh && \  
/usr/bin/mysql_install_db --user=mysql && \  
mkdir /run/mysqld && \  
mkdir -p /var/tmp/mysql && \  
chown mysql:mysql /var/tmp/mysql  
  
EXPOSE 3306  
WORKDIR /tmp  
  
ENTRYPOINT ["mysqld"]  

