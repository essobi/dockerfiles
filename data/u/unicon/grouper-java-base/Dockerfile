FROM centos:centos7  
  
MAINTAINER John Gasper <jgasper@unicon.net>  
  
ENV JAVA_HOME=/opt/openjdk7  
  
RUN java_version=8.0.163; \  
zulu_version=8.28.0.1; \  
yum update -y \  
&& yum install -y wget tar \  
&& yum clean all \  
\  
&& echo 'Downloading the OpenJDK Zulu...' \  
&& wget -q http://cdn.azul.com/zulu/bin/zulu$zulu_version-jdk$java_version-
linux_x64.tar.gz \  
&& echo "9c02c89f37d217d229203e59b57246a8 zulu$zulu_version-jdk$java_version-
linux_x64.tar.gz" | md5sum -c - \  
&& tar -zxvf zulu$zulu_version-jdk$java_version-linux_x64.tar.gz -C /opt \  
&& ln -s /opt/zulu$zulu_version-jdk$java_version-linux_x64 $JAVA_HOME \  
&& rm zulu$zulu_version-jdk$java_version-linux_x64.tar.gz  

