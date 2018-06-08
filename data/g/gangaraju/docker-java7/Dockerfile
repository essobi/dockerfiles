FROM centos:centos7  
Run yum install -y wget;yum -y clean all  
#java7  
RUN wget --continue --no-check-certificate --header "Cookie: oraclelicense=a"
-O jdk-linux-x64.rpm "http://download.oracle.com/otn-
pub/java/jdk/7u67-b01/jdk-7u67-linux-x64.rpm"  
RUN yum install -y jdk-linux-x64.rpm;yum -y clean all  
RUN rm jdk*.rpm  
ENV JAVA_HOME /usr/java/default  
  

