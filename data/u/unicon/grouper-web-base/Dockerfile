FROM unicon/grouper-api:2.2.2  
  
MAINTAINER John Gasper <jgasper@unicon.net>  
  
RUN yum update -y \  
&& yum install -y wget unzip dos2unix \  
&& yum clean all \  
\  
&& echo 'Downloading Tomcat...' \  
&& wget -q https://archive.apache.org/dist/tomcat/tomcat-6/v6.0.44/bin/apache-
tomcat-6.0.44.zip \  
&& echo "409e93f383ec476cde4c9b87f2427dbf apache-tomcat-6.0.44.zip" | md5sum
-c - \  
&& unzip apache-tomcat-6.0.44.zip -d /opt \  
&& rm apache-tomcat-6.0.44.zip \  
&& find /opt/apache-tomcat-6.0.44/bin/ -name "*.sh" -exec chmod a+x {} \; \  
\  
&& echo 'Downloading Ant...'\  
&& wget -q https://archive.apache.org/dist/ant/binaries/apache-
ant-1.9.5-bin.zip \  
&& unzip apache-ant-1.9.5-bin.zip -d /opt \  
&& echo "8c4193db6ac91c3f792a04715f8e9a82ef628daf apache-ant-1.9.5-bin.zip" |
sha1sum -c - \  
&& rm -rf apache-ant-1.9.5-bin.zip /opt/apache-tomcat-6.0.44/webapps/* \  
&& chmod +x /opt/apache-ant-1.9.5/bin/ant  
  
EXPOSE 8080  
  
CMD ["/opt/apache-tomcat-6.0.44/bin/catalina.sh", "run"]  

