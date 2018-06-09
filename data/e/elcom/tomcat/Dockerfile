FROM anapsix/docker-oracle-java8  
MAINTAINER LWB  
  
ENV JAVA_MAJOR 8  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.31  
ENV TOMCAT_PORT 8080  
ADD ./run.sh /usr/local/bin/run  
  
RUN wget -O /tmp/tomcat.tar.gz
http://www.us.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
cd /opt && \  
tar zxf /tmp/tomcat.tar.gz && \  
rm /tmp/tomcat.tar.gz && \  
mv /opt/apache-tomcat* /opt/tomcat && \  
mkdir -p /var/lib/tomcat && \  
sed -i "s!<Connector port=\"8080\"!<Connector port=\"${TOMCAT_PORT}\"
URIEncoding=\"UTF-8\"!g" /opt/tomcat/conf/server.xml && \  
sed -i "s!<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>!<?xml
version=\"1.0\" encoding=\"UTF-8\"?>!g" /opt/tomcat/conf/web.xml && \  
chmod +x /usr/local/bin/run && \  
echo "JAVA_HOME=${JAVA_HOME}" >> /etc/default/tomcat${TOMCAT_MAJOR}  
  
RUN mkdir -p /opt/tomcat/conf.bak && \  
mkdir -p /opt/tomcat/lib.bak  
  
EXPOSE ${TOMCAT_PORT}  
  
VOLUME /opt/tomcat/webapps  
VOLUME /opt/tomcat/conf.bak  
VOLUME /opt/tomcat/lib.bak  
  
CMD /usr/local/bin/run  

