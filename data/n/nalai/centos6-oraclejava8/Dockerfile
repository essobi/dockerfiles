FROM centos:centos6  
MAINTAINER Nathaniel Lai "nathaniel.lai@retrievercommunications.com"  
#Install wget and install Java 8  
RUN yum -y install wget  
RUN wget --no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-pub/java/jdk/8u31-b13/jre-8u31-linux-x64.rpm"
\  
-O /tmp/jre-8u31-linux-x64.rpm  
RUN chmod 755 /tmp/jre-8u31-linux-x64.rpm && \  
rpm -ivh /tmp/jre-8u31-linux-x64.rpm && \  
rm /tmp/jre-8u31-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/default  

