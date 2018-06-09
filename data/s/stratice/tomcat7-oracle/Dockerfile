FROM stackbrew/debian:jessie  
MAINTAINER Arcus "http://arcus.io"  
RUN apt-get update  
  
ENV TOMCATVER 7.0.57  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install patch unzip wget  
RUN (wget --progress=dot --no-check-certificate -O /tmp/server-
jre-7u71-linux-x64.tar.gz --header "Cookie: oraclelicense=a"
http://download.oracle.com/otn-pub/java/jdk/7u71-b14/server-
jre-7u71-linux-x64.tar.gz &&\  
echo "2e29846da3297c9b2469d69017363bd7 /tmp/server-jre-7u71-linux-x64.tar.gz"
| md5sum -c > /dev/null 2>&1 || echo "ERROR: MD5SUM MISMATCH" &&\  
tar xzf /tmp/server-jre-7u71-linux-x64.tar.gz &&\  
mkdir -p /usr/lib/jvm/java-7-oracle &&\  
mv jdk1.7.0_71/jre /usr/lib/jvm/java-7-oracle/jre &&\  
rm -rf jdk1.7.0_71 && rm /tmp/server-jre-7u71-linux-x64.tar.gz &&\  
chown root:root -R /usr/lib/jvm/java-7-oracle &&\  
update-alternatives --install /usr/bin/java java
/usr/lib/jvm/java-7-oracle/jre/bin/java 1 &&\  
update-alternatives --set java /usr/lib/jvm/java-7-oracle/jre/bin/java)  
  
RUN (wget -O /tmp/tomcat7.tar.gz
http://www.us.apache.org/dist/tomcat/tomcat-7/v${TOMCATVER}/bin/apache-
tomcat-${TOMCATVER}.tar.gz &&\  
cd /opt &&\  
tar zxf /tmp/tomcat7.tar.gz &&\  
rm /tmp/tomcat7.tar.gz &&\  
mv /opt/apache-tomcat* /opt/tomcat &&\  
rm -rf /opt/tomcat/webapps/*)  
  
ADD ./run.sh /usr/local/bin/run  
ADD server.xml.patch /tmp/server.xml.patch  
RUN (patch -N /opt/tomcat/conf/server.xml /tmp/server.xml.patch && rm
/tmp/server.xml.patch)  
  
ADD newrelic_agent3.8.1.zip /tmp/newrelic_agent3.8.1.zip  
RUN (cd /opt/tomcat &&\  
unzip /tmp/newrelic_agent3.8.1.zip &&\  
rm /tmp/newrelic_agent3.8.1.zip &&\  
cd /opt/tomcat/newrelic &&\  
java -jar newrelic.jar install)  
ADD newrelic.yml /opt/tomcat/newrelic/newrelic.yml  
  
EXPOSE 8080  
CMD ["/usr/local/bin/run"]  

