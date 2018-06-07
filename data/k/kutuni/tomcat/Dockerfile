FROM kutuni/openjdk:1.8-alpine  
  
MAINTAINER kutuni  
  
ENV TOMCAT_MAJOR=8 \  
TOMCAT_VERSION=8.5.9 \  
TOMCAT_HOME=/tomcat \  
CATALINA_HOME=/tomcat \  
CATALINA_OUT=/dev/null  
  
RUN echo
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz  
  
COPY server.xml /  
COPY context.xml /  
ADD catalina.properties /  
  
RUN \  
curl -jksSL -o /tmp/apache-tomcat.tar.gz
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
gunzip /tmp/apache-tomcat.tar.gz && \  
tar -C / -xf /tmp/apache-tomcat.tar && \  
mv /apache-tomcat-${TOMCAT_VERSION} ${TOMCAT_HOME} && \  
mv /server.xml ${TOMCAT_HOME}/conf && \  
mv /context.xml ${TOMCAT_HOME}/conf && \  
mv /catalina.properties ${TOMCAT_HOME}/conf && \  
cp -a ${TOMCAT_HOME}/conf ${TOMCAT_HOME}/conf.original && \  
rm -rf ${TOMCAT_HOME}/webapps/* && \  
rm -rf ${TOMCAT_HOME}/bin/*.bat  
  
VOLUME ["/tomcat/webapps"]  
VOLUME ["/tomcat/conf"]  
EXPOSE 8000  
ADD run /  
ADD docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
HEALTHCHECK \--timeout=2s CMD curl -f http://127.0.0.1:8000  
  
CMD ["/run"]  
  
RUN chmod +x run docker-entrypoint.sh  

