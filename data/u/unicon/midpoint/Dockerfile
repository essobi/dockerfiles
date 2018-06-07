FROM centos:centos7  
  
MAINTAINER John Gasper <jgasper@unicon.net>  
  
ENV JAVA_HOME=/opt/openjdk8  
  
RUN java_version=8.0.121; \  
zulu_version=8.20.0.5; \  
yum update -y \  
&& yum install -y wget tar graphviz \  
&& yum clean all \  
\  
&& echo 'Downloading the OpenJDK Zulu...' \  
&& wget -q http://cdn.azul.com/zulu/bin/zulu$zulu_version-jdk$java_version-
linux_x64.tar.gz \  
&& echo "e5f4b1d997e50ffe4998c68c8ec45403 zulu$zulu_version-jdk$java_version-
linux_x64.tar.gz" | md5sum -c - \  
&& tar -zxvf zulu$zulu_version-jdk$java_version-linux_x64.tar.gz -C /opt \  
&& ln -s /opt/zulu$zulu_version-jdk$java_version-linux_x64 $JAVA_HOME \  
&& rm zulu$zulu_version-jdk$java_version-linux_x64.tar.gz  
  
#Install Tomcat  
RUN tomcat_version=8.0.39; \  
tomcat_hash=18c54a81e05df39dec9ac02b143875a29b5502d5; \  
wget
https://archive.apache.org/dist/tomcat/tomcat-8/v$tomcat_version/bin/apache-
tomcat-$tomcat_version.tar.gz \  
&& echo "$tomcat_hash apache-tomcat-$tomcat_version.tar.gz" | sha1sum -c - \  
&& tar -zxvf apache-tomcat-$tomcat_version.tar.gz -C /opt \  
&& rm apache-tomcat-$tomcat_version.tar.gz \  
&& ln -sf /opt/apache-tomcat-$tomcat_version/ /opt/tomcat \  
&& rm -rf /opt/tomcat/webapps/  
  
#Install midPoint  
RUN midpoint_version=3.6; \  
wget
https://evolveum.com/downloads/midpoint/$midpoint_version/midpoint-$midpoint_version-
dist.tar.gz \  
&& tar -zxvf midpoint-$midpoint_version-dist.tar.gz -C /opt \  
&& rm midpoint-$midpoint_version-dist.tar.gz \  
&& ln -sf /opt/midpoint-$midpoint_version/ /opt/midpoint \  
&& mkdir -p /opt/tomcat/webapps/midpoint/ \  
&& cd /opt/tomcat/webapps/midpoint/ \  
&& /opt/openjdk8/bin/jar xvf /opt/midpoint/war/midpoint.war \  
&& rm /opt/midpoint/war/midpoint.war  
  
COPY opt-tomcat/ /opt/tomcat/  
COPY usr-local-bin/ /usr/local/bin/  
  
RUN chmod 750 /usr/local/bin/run-tomcat.sh  
  
EXPOSE 8080  
CMD run-tomcat.sh

