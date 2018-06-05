FROM ubuntu:14.04  
MAINTAINER Prognosio  
  
# install java 8  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections && \  
echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-
selections  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer  
  
# install dependencies  
RUN apt-get update && \  
apt-get install -y telnet curl unzip wget docker.io git mercurial subversion
bzr  
  
# install bamboo  
ENV BAMBOO_VERSION 5.9.7  
RUN curl -L -o /tmp/atlassian-bamboo-${BAMBOO_VERSION}.tar.gz
https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz && \  
tar -xzvf /tmp/atlassian-bamboo-${BAMBOO_VERSION}.tar.gz && \  
rm -rf /tmp/atlassian* && \  
ln -s /atlassian-bamboo-${BAMBOO_VERSION} /atlassian-bamboo  
  
# setup external database  
ENV MYSQL_VERSION 5.1.37  
RUN curl -L -o /tmp/mysql.tar.gz
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_VERSION}.tar.gz && \  
cd /atlassian-bamboo/lib && \  
tar -xzvf /tmp/mysql.tar.gz mysql-connector-java-${MYSQL_VERSION}/mysql-
connector-java-5.1.37-bin.jar && \  
mv mysql-connector-java-${MYSQL_VERSION}/mysql-connector-java-5.1.37-bin.jar .
&& \  
rmdir mysql-connector-java-${MYSQL_VERSION} && \  
rm -f /tmp/mysql.tar.gz  
  
# configure bamboo  
RUN echo "bamboo.home = /bamboo-data" > /atlassian-bamboo/atlassian-
bamboo/WEB-INF/classes/bamboo-init.properties  
  
VOLUME /bamboo-data  
  
ADD bamboo.cfg.xml /bamboo-data/bamboo.cfg.xml  
  
EXPOSE 8085  
EXPOSE 54663  
CMD [ "/atlassian-bamboo/bin/catalina.sh", "run" ]  
  

