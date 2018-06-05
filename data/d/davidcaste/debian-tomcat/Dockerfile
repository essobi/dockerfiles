FROM davidcaste/debian-oracle-java:jdk7  
  
MAINTAINER David Castellanos <davidcaste@gmail.com>  
  
ENV TOMCAT_MAJOR=8 \  
TOMCAT_VERSION=8.0.33 \  
TOMCAT_HOME=/opt/tomcat \  
CATALINA_HOME=/opt/tomcat \  
CATALINA_OUT=/dev/null  
  
RUN apt-get update -q && \  
apt-get install -q -y --no-install-recommends curl && \  
curl -jksSL -o /tmp/apache-tomcat.tar.gz
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
gunzip /tmp/apache-tomcat.tar.gz && \  
tar -C /opt -xf /tmp/apache-tomcat.tar && \  
ln -s /opt/apache-tomcat-${TOMCAT_VERSION} ${TOMCAT_HOME} && \  
rm -rf ${TOMCAT_HOME}/webapps/* && \  
apt-get remove --purge -y curl && \  
apt-get autoremove --purge -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY logging.properties ${TOMCAT_HOME}/conf/logging.properties  
COPY server.xml ${TOMCAT_HOME}/conf/server.xml  
  
VOLUME ["/logs"]  
EXPOSE 8080  

