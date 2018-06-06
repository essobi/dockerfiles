FROM mysql/mysql-server:5.7  
MAINTAINER Ultical Team team@ultical.com  
  
# install java and liquibase and execute it  
# RUN yum -y install java-1.8.0-openjdk-headless wget tar \  
# && wget -q
https://github.com/liquibase/liquibase/releases/download/liquibase-
parent-3.5.3/liquibase-3.5.3-bin.tar.gz \  
# && wget -q https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.44.tar.gz \  
# && tar xfz liquibase-3.5.3-bin.tar.gz \  
# && tar xfz mysql-connector-java-5.1.44.tar.gz \  
# && yum -y erase wget tar \  
# && rm -rf /var/cache/yum  
# setting JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-openjdk  
  
# setting some enviroment variables the base image responds to  
ENV MYSQL_RANDOM_ROOT_PASSWORD yes  
ENV MYSQL_USER ultical  
ENV MYSQL_PASSWORD ultical  
ENV MYSQL_DATABASE ultical  
  
# adding files  
ADD changelog.sql /docker-entrypoint-initdb.d/  
ADD test-data.sql /docker-entrypoint-initdb.d/

