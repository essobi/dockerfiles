FROM centos:7  
MAINTAINER Saif Charaniya <saif.charaniya@fuseforward.com>  
  
RUN yum update  
RUN yum install -y wget  
RUN wget --no-cookies --no-check-certificate --header \  
"Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-
securebackup-cookie" \  
"http://download.oracle.com/otn-pub/java/jdk/8u92-b14/jdk-8u92-linux-x64.rpm"  
RUN rpm -ivh jdk-8u92-linux-x64.rpm  
RUN rm jdk-8u92-linux-x64.rpm  
  
RUN yum install -y which  
  
RUN curl -O http://apache.mirror.rafal.ca/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz  
RUN tar -xvf apache-maven-3.3.9-bin.tar.gz  
RUN mv apache-maven-3.3.9 /opt/maven  
RUN rm -rf apache-maven-3.3.9-bin.tar.gz  
RUN ln -s /opt/maven/bin/mvn /usr/bin/mvn  
RUN touch /etc/profile.d/maven.sh  
RUN printf
'#!/bin/bash\nMAVEN_HOME=/var/maven\nPATH=$MAVEN_HOME/bin:$PATH\nexport PATH
MAVEN_HOME\nexport CLASSPATH=.' > /etc/profile.d/maven.sh  
RUN chmod +x /etc/profile.d/maven.sh  
RUN source /etc/profile.d/maven.sh

