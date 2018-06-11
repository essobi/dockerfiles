FROM centos:centos6.6  
RUN yum -y update  
RUN yum -y install wget vim  
ENV JAVA_VERSION_CODE 8u51  
  
RUN wget -O "/var/tmp/java.rpm" \--no-check-certificate --no-cookies --header
"Cookie: oraclelicense=accept-securebackup-cookie" \--no-verbose
http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION_CODE-b16/jdk-$JAVA_VERSION_CODE-linux-x64.rpm &&rpm
-ivh /var/tmp/java.rpm && rm /var/tmp/java.rpm  
ADD setENV.sh /etc/profile.d/setENV.sh  

