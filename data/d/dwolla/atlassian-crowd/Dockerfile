FROM tomcat:8.5-alpine  
MAINTAINER Dwolla Engineering <dev+crowd@dwolla.com>  
  
LABEL org.label-schema.vcs-url="https://github.com/Dwolla/atlassian-crowd-
docker"  
  
ENV CROWD_HOME=/opt/crowd/home \  
CROWD_INSTALL=/opt/crowd/webapp \  
CROWD_USER=crowd \  
CROWD_GROUP=crowd \  
CROWD_VERSION=2.9.1 \  
MYSQL_CONNECTOR_VERSION=5.1.39  
EXPOSE 8443  
COPY redirector /opt/redirector  
  
RUN apk update && \  
apk add --update curl ca-certificates jq groff less python py-pip bash openssl
openjdk8="$JAVA_ALPINE_VERSION" && \  
curl https://www.digicert.com/CACerts/GTECyberTrustGlobalRoot.crt | openssl
x509 -inform der -outform pem -out /usr/local/share/ca-
certificates/GTECyberTrustGlobalRoot.crt && \  
update-ca-certificates && \  
rm -rf ${CATALINA_HOME}/webapps/* && \  
mkdir -p ${CROWD_HOME} ${CROWD_INSTALL}
${CATALINA_HOME}/conf/Catalina/localhost && \  
cd /opt && \  
curl -vL -o ${CROWD_INSTALL}/crowd.war
https://www.atlassian.com/software/crowd/downloads/binary/atlassian-
crowd-${CROWD_VERSION}-war.zip && \  
cd ${CROWD_INSTALL} && unzip crowd.war && rm crowd.war && cd \- && \  
curl -vL -o /tmp/mysql-connector.tgz
https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz && \  
tar xzf /tmp/mysql-connector.tgz mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar && \  
mv mysql-connector-java-5.1.39/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar ${CATALINA_HOME}/lib/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar && \  
pip install awscli && \  
sed -i
s_securerandom.source=file:/dev/random_securerandom.source=file:/dev/urandom_
$JAVA_HOME/lib/security/java.security && \  
curl -vL "https://dl.bintray.com/sbt/native-
packages/sbt/0.13.12/sbt-0.13.12.tgz" | \  
gunzip | tar -x -C /usr/local && \  
cd /opt/redirector && \  
/usr/local/sbt/bin/sbt clean test package && \  
mkdir -p ${CATALINA_HOME}/webapps/ROOT && unzip -d
${CATALINA_HOME}/webapps/ROOT target/scala-2.11/*.war && \  
apk --purge -v del py-pip openjdk8 && \  
rm -rf /var/cache/apk/* /opt/redirector /usr/local/sbt /tmp/* /root/.ivy2/
/root/.sbt/ /root/.cache/  
  
COPY context.xml.tmpl /opt/context.xml.tmpl  
COPY server.xml ${CATALINA_HOME}/conf/server.xml  
COPY crowd.cfg.tmpl /opt/crowd.cfg.tmpl  
COPY start.sh /opt/start.sh  
COPY jars/* ${CATALINA_HOME}/lib/  
  
ENTRYPOINT ["/opt/start.sh"]  
CMD ["run"]  

