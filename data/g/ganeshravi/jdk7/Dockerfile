FROM centos:centos7  
MAINTAINER Ganesh Ravi <ganesh.reddy.22@gmail.com>  
  
RUN yum -y install wget  
  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/7u67-b01/jdk-7u67-linux-x64.tar.gz  
  
RUN yum -y install tar  
  
RUN tar -zxvf jdk-7u67-linux-x64.tar.gz  
  
RUN mv -f jdk1.7.0_67/ /opt/  
  
ENV JAVA_HOME /opt/jdk1.7.0_67  
  
RUN ln -f -s $JAVA_HOME/bin/* /usr/bin/  

