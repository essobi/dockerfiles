FROM oraclelinux:latest  
  
MAINTAINER Cleber Barcelos <barcelos.cbc@gmail.com>  
LABEL Description="Banco de Dados MySql " Vendor="ASW Puc Minas OF05"
Version="1.0"  
  
ENV PACKAGE_URL
https://repo.mysql.com/yum/mysql-5.7-community/docker/x86_64/mysql-community-
server-minimal-5.7.13-1.el7.x86_64.rpm  
  
# Install server  
RUN rpmkeys --import http://repo.mysql.com/RPM-GPG-KEY-mysql \  
&& yum install -y $PACKAGE_URL \  
&& yum install -y libpwquality \  
&& rm -rf /var/cache/yum/*  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
VOLUME /var/lib/mysql  
  
COPY scripts /docker-entrypoint-initdb.d  
  
ADD docker-entrypoint.sh /entrypoint.sh  
RUN sed -i 's/\r//' /entrypoint.sh  
ENV MYSQL_ROOT_PASSWORD=root  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306 33060  
CMD ["mysqld"]

