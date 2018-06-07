FROM centos  
  
MAINTAINER Rahul Somasunderam  
  
RUN yum install -y wget  
  
RUN cd /tmp; wget --no-cookies --no-check-certificate \  
\--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.rpm";
\  
rpm -Uvh jdk-7u65-linux-x64.rpm; \  
echo "export JAVA_HOME=/usr/java/default" > ~/.bashrc; \  
source ~/.bashrc  

