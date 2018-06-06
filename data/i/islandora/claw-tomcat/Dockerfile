FROM islandora/claw-oracle-jdk  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
ARG TOMCAT_VERSION="7.0.69"  
EXPOSE 8080  
ENV CATALINA_HOME=/opt/tomcat \  
CATALINA_BASE=/opt/tomcat \  
CATALINA_OPTS="-server -XX:+CMSClassUnloadingEnabled -Djava.awt.headless=true
-Djava.security.egd=file:/dev/urandom" \  
PATH=${PATH}:/opt/tomcat/bin  
  
RUN addgroup -g 1000 tomcat && \  
adduser -u 100 -s /sbin/nologin -G tomcat -SDH -h ${CATALINA_HOME} tomcat && \  
curl -L
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_VERSION%%.*}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz | \  
tar -xzf - -C /tmp && \  
mv /tmp/apache-tomcat-${TOMCAT_VERSION} ${CATALINA_HOME} && \  
rm -rf ${CATALINA_HOME}/webapps/docs && \  
rm -rf ${CATALINA_HOME}/webapps/examples && \  
cleanup  
  
COPY rootfs /  

