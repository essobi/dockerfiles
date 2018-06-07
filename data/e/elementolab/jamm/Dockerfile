# Dockerfile for JAMM (JAVA, Apache, MySQL, Maven)  
FROM centos:6.7  
MAINTAINER Alexandros Sigaras <als2076@med.cornell.edu>  
#===========================#  
# CentOS Preparation #  
#===========================#  
RUN yum groupinstall -y "Development Tools"; \  
yum install -y man vi nano git wget tar gcc-c++ openssl-devel make MySQL-
python; \  
yum -y clean all  
WORKDIR /opt  
#=======================#  
# JAVA 1.8.0_77 #  
#=======================#  
RUN wget --no-check-certificate --no-cookies --header 'Cookie:
oraclelicense=accept-securebackup-cookie' http://download.oracle.com/otn-
pub/java/jdk/8u77-b03/jdk-8u77-linux-x64.rpm; \  
rpm -ivh jdk-8u77-linux-x64.rpm; \  
rm jdk-8u77-linux-x64.rpm; \  
echo "export JAVA_HOME=/usr/java/jdk1.8.0_77" >> /root/.bashrc; \  
echo "export JRE_HOME=/usr/java/jdk1.8.0_77/jre" >> /root/.bashrc; \  
echo "export
PATH=$PATH:/usr/java/jdk1.8.0_77/bin:/usr/java/jdk1.8.0_77/jre/bin" >>
/root/.bashrc;  
#=======================#  
# Apache Tomcat 8.0.33 #  
#=======================#  
RUN wget http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.33/bin/apache-
tomcat-8.0.33.tar.gz; \  
tar xzf apache-tomcat-8.0.33.tar.gz; \  
rm --force apache-tomcat-8.0.33.tar.gz; \  
echo "export CATALINA_HOME=/opt/apache-tomcat-8.0.33" >> /root/.bashrc; \  
. /root/.bashrc; rm -rf $CATALINA_HOME/webapps/examples  
#=======================#  
# MYSQL & J/Connector #  
#=======================#  
RUN wget http://dev.mysql.com/get/mysql57-community-release-el6-7.noarch.rpm;
\  
yum localinstall -y mysql57-community-release-el6-*.noarch.rpm; \  
yum install -y mysql-community-server; \  
yum -y clean all; \  
rm --force mysql57-community-release-el6-*.noarch.rpm; \  
touch /etc/sysconfig/network; \  
chkconfig mysqld on  
RUN wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.38.tar.gz; \  
tar xzvf mysql-connector-java-5.1.38.tar.gz; \  
rm --force mysql-connector-java-5.1.38.tar.gz; \  
cp /opt/mysql-connector-java-5.1.38/mysql-connector-java-5.1.38-bin.jar
/opt/apache-tomcat-8.0.33/lib/; \  
. /root/.bashrc; echo "export CLASSPATH=/opt/apache-tomcat-8.0.33/lib/mysql-
connector-java-5.1.38-bin.jar" >> $CATALINA_HOME/lib/setenv.sh  
#=======================#  
# Maven 3.3.9 #  
#=======================#  
RUN wget http://mirrors.koehn.com/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz; \  
tar xzf apache-maven-3.3.9-bin.tar.gz; \  
rm --force apache-maven-3.3.9-bin.tar.gz; \  
mv apache-maven-3.3.9 /usr/local/apache-maven; \  
echo "export M2_HOME=/usr/local/apache-maven" >> /root/.bashrc; \  
. /root/.bashrc; echo "export M2=$M2_HOME/bin" >> /root/.bashrc; \  
. /root/.bashrc; echo "export PATH=$M2:$PATH" >> /root/.bashrc;  
WORKDIR /  
#===========================================================================================#

