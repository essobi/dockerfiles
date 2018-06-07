  
FROM centos:centos7  
  
MAINTAINER Sergei Korneev <Sergei_Korneev@epam.com>  
  
RUN yum -y install wget && \  
wget --progress=bar:force --no-check-certificate --no-cookies --header
"Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/7u72-b14/jre-7u72-linux-x64.rpm &&
\  
echo "e48cdd20ee993726005dbaea26ec0dcc jre-7u72-linux-x64.rpm" >> MD5SUM && \  
md5sum -c MD5SUM && \  
rpm -Uvh jre-7u72-linux-x64.rpm && \  
yum -y remove wget && \  
rm -f jre-7u72-linux-x64.rpm MD5SUM  

