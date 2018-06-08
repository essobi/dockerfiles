FROM phenompeople/centos-sunjdk:8u152  
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com"  
ARG TOMCAT_VERSION=8.0.47  
ARG APP_HOME=/opt/deployment  
ARG TOMCAT_HOME=${APP_HOME}/apache-tomcat  
  
RUN wget -q -O /tmp/apache-tomcat.tar.gz
https://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
tar xfz /tmp/apache-tomcat.tar.gz -C ${APP_HOME} && \  
mv ${APP_HOME}/apache-tomcat-${TOMCAT_VERSION} ${TOMCAT_HOME} && \  
rm -rf /tmp/apache-tomcat.tar.gz && \  
rm -rf ${TOMCAT_HOME}/webapps/* && \  
rm -rf ${TOMCAT_HOME}/bin/*.bat && \  
rm -rf ${TOMCAT_HOME}/{LICENSE,NOTICE,RELEASE-NOTES,RUNNING.txt}  
  
ENV CATALINA_HOME=${TOMCAT_HOME} \  
CATALINA_BASE=${TOMCAT_HOME}  
ENV CATALINA_OUT=${CATALINA_BASE}/logs/catalina.out \  
CATALINA_PID=${CATALINA_BASE}/bin/catalina.pid  
EXPOSE 8080 8005 8009 8443  

