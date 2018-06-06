FROM islandora/claw-tomcat:oracle-jdk  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
ARG SOLR_VERSION="4.10.4"  
ARG SOLR_DEPENDENCIES="log4j-1.2.17.jar slf4j-api-1.7.6.jar
slf4j-log4j12-1.7.6.jar"  
ENV SOLR_HOME=/opt/solr  
  
RUN curl -L
http://archive.apache.org/dist/lucene/solr/${SOLR_VERSION}/solr-${SOLR_VERSION}.tgz
| \  
tar -xzf - -C /tmp && \  
mkdir ${CATALINA_BASE}/webapps/solr && \  
cp /tmp/solr-${SOLR_VERSION}/dist/solr-${SOLR_VERSION}.war
${CATALINA_BASE}/webapps/solr.war && \  
unzip -o ${CATALINA_BASE}/webapps/solr.war -d ${CATALINA_BASE}/webapps/solr &&
\  
for dep in ${SOLR_DEPENDENCIES}; do \  
cp /tmp/solr-${SOLR_VERSION}/example/lib/ext/$dep ${CATALINA_BASE}/lib; \  
done && \  
curl -o ${CATALINA_BASE}/lib/commons-logging-1.1.2.jar \  
-L http://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.2/commons-logging-1.1.2.jar && \  
mkdir ${SOLR_HOME} && \  
cp -a /tmp/solr-${SOLR_VERSION}/example/solr/* ${SOLR_HOME}/ && \  
curl -L https://ftp.drupal.org/files/projects/apachesolr-7.x-1.8.tar.gz | \  
tar -xzf - -C /tmp && \  
cp -r /tmp/apachesolr/solr-conf/solr-4.x/* ${SOLR_HOME}/collection1/conf && \  
mkdir ${SOLR_HOME}/collection1/data && \  
chown -R tomcat:tomcat ${SOLR_HOME} && \  
rm -rf ${CATALINA_HOME}/webapps/*.war && \  
cleanup  
  
COPY rootfs /  

