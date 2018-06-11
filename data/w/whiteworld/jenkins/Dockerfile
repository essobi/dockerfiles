FROM jenkins:1.609.1  
MAINTAINER White World "ljq258@gmail.com"  
USER root  
# Install maven  
RUN curl -L -O
http://mirrors.cnnic.cn/apache/maven/maven-3/3.3.3/binaries/apache-
maven-3.3.3-bin.tar.gz && tar xf apache-maven-3.3.3-bin.tar.gz -C /opt  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/7u67-b01/jdk-7u67-linux-x64.tar.gz && tar xf
jdk-7u67-linux-x64.tar.gz -C /opt  
USER jenkins  
# Install plugins  
# COPY plugins.txt /usr/share/jenkins/  
# RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
# Set timezone  
# ENV TZ Asia/Shanghai  

