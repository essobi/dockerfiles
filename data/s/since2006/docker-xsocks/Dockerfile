  
FROM jdeathe/centos-ssh:centos-7  
RUN yum -y install wget unzip  
  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.rpm"  
  
RUN rpm -ivh jdk-8u102-linux-x64.rpm  
  
RUN rm -f jdk-8u102-linux-x64.rpm  
  

