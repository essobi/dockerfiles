FROM ubuntu:14.04  
MAINTAINER Arcus "http://arcus.io"  
ENV DEBIAN_FRONTEND noninteractive  
ENV JAVA_HOME /opt/jdk/jre  
ENV PATH $PATH:/opt/jdk/jre/bin  
ENV LIFERAY_HOME /opt/liferay-portal-6.2-ce-ga2  
ENV CATALINA_OPTS -Dfile.encoding=UTF8 -Djava.net.preferIPv4Stack=true
-Dorg.apache.catalina.loader.WebappClassLoader.ENABLE_CLEAR_REFERENCES=false
-Duser.timezone=GMT -Xmx1024m -XX:MaxPermSize=256m -Dexternal-
properties=portal-db.properties -Ddb_host=$DB_HOST -Ddb_port=$DB_PORT
-Ddb_user=$DB_USER -Ddb_pass=$DB_PASS -Ddb_name=$DB_NAME  
RUN apt-get update && \  
apt-get install -y wget unzip  
RUN (cd /tmp && wget --progress=dot --no-check-certificate -O jdk.tar.gz
\--header "Cookie: oraclelicense=a" http://download.oracle.com/otn-
pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.tar.gz && \  
tar zxf jdk.tar.gz && mv jdk1.7.0_65 /opt/jdk)  
  
RUN (cd /tmp && \  
wget
http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.2.1%20GA2/liferay-
portal-tomcat-6.2-ce-ga2-20140319114139101.zip -O liferay.zip && \  
unzip liferay.zip -d /opt && \  
rm -f liferay.zip)  
ADD conf/portal-bundle.properties $LIFERAY_HOME/portal-bundle.properties  
ADD conf/portal-db.properties $LIFERAY_HOME/portal-db.properties  
EXPOSE 8080  
ENTRYPOINT ["/opt/liferay-portal-6.2-ce-ga2/tomcat-7.0.42/bin/catalina.sh"]  
CMD ["run"]  

