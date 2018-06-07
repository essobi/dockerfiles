FROM tomcat:8-jre8  
  
MAINTAINER Clement Laforet  
  
  
RUN rm -fr ${CATALINA_HOME}/webapps/*  
  
ENV CONFD_VERSION 0.11.0  
RUN mkdir -p /usr/local/bin/ && \  
wget -q -nv -O /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 &&\  
chmod +x /usr/local/bin/confd  
  
ENV MYSQL_CONNECTOR_VERSION=5.1.39  
RUN wget -q -nv -O ${CATALINA_HOME}/lib/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.jar \  
http://central.maven.org/maven2/mysql/mysql-connector-
java/${MYSQL_CONNECTOR_VERSION}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.jar  
  
ENV METACAT_CATALOG_DIR=/etc/catalog \  
MYSQL_HOST=localhost \  
MYSQL_DATABASE=metacat \  
MYSQL_USER=metacat \  
MYSQL_PASSWORD=metacat  
  
  
ENV METACAT_VERSION=0.1.24  
RUN mkdir /metacat/ && \  
wget -q -nv -O /metacat/metacat.war \  
http://central.maven.org/maven2/com/netflix/metacat/metacat-
server/${METACAT_VERSION}/metacat-server-${METACAT_VERSION}.war  
  
ADD confd /etc/confd  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

