FROM guligo/jdk-maven-ant-tomcat:latest  
  
#######  
# MySQL  
#######  
# Preparation  
ENV MYSQL_MAJOR 5.6  
ENV MYSQL_VERSION 5.6.25  
# Installation  
RUN echo "deb http://repo.mysql.com/apt/debian/ wheezy mysql-${MYSQL_MAJOR}" >
/etc/apt/sources.list.d/mysql.list  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
A4A9406876FCBD3C456770C88C718D3B5072E1F5  
RUN { \  
echo mysql-community-server mysql-community-server/data-dir select ''; \  
echo mysql-community-server mysql-community-server/root-pass password ''; \  
echo mysql-community-server mysql-community-server/re-root-pass password ''; \  
echo mysql-community-server mysql-community-server/remove-test-db select
false; \  
} | debconf-set-selections  
RUN apt-get update  
RUN apt-get install -y mysql-server="${MYSQL_VERSION}"*  
  

