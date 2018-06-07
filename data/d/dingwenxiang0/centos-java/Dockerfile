FROM centos:7  
  
MAINTAINER Ding Wen Xiang "624380857@qq.com"  
  
ARG JAVA_MINOR_VERSION=121  
  
ENV JAVA_HOME=/app/tools/java/jdk  
ENV PATH=$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin  
ENV CLASSPATH=.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$CLASSPATH  
  
ADD https://raw.githubusercontent.com/dingwenxiang0/docker-centos-
java/master/oracle_download_cookies /tmp/oracle_download_cookies  
RUN yum -y update \  
&& yum -y install wget \  
&& OHS_COOKIE=`cat /tmp/oracle_download_cookies` \  
&& mkdir -p /app/tools/java \  
&& cd /app/tools/java \  
&& wget --no-check-certificate --no-cookies --header "Cookie: $OHS_COOKIE
oraclelicense=accept-securebackup-cookie;"
http://download.oracle.com/otn/java/jdk/8u$JAVA_MINOR_VERSION-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u$JAVA_MINOR_VERSION-
linux-x64.tar.gz \  
&& tar -zxf jdk-8u$JAVA_MINOR_VERSION-linux-x64.tar.gz \  
&& ln -s /app/tools/java/jdk1.8.0_$JAVA_MINOR_VERSION /app/tools/java/jdk \  
&& yum -y remove wget \  
&& yum clean all \  
&& java -version \  
&& rm -rf jdk-8u$JAVA_MINOR_VERSION-linux-x64.tar.gz \  
&& rm -rf /tmp/oracle_download_cookies  
  
CMD ["/bin/bash"]

