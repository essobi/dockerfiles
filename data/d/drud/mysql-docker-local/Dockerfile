FROM oraclelinux:latest  
  
ENV PACKAGE_URL
https://repo.mysql.com/yum/mysql-5.7-community/docker/x86_64/mysql-community-
server-minimal-5.7.13-1.el7.x86_64.rpm  
ENV MYSQL_DATABASE data  
ENV MYSQL_ROOT_PASSWORD root  
ENV MYSQL_MAX_ALLOWED_PACKET 16m  
  
# Install server  
RUN rpmkeys --import http://repo.mysql.com/RPM-GPG-KEY-mysql \  
&& yum install -y $PACKAGE_URL \  
&& yum install -y libpwquality \  
&& rm -rf /var/cache/yum/* \  
&& rm -rf /var/lib/mysql \  
&& mkdir -p /var/lib/mysql  
  
RUN mkdir /docker-entrypoint-initdb.data  
ADD files /  
VOLUME /var/lib/mysql  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306 33060  
CMD ["mysqld"]  
  

