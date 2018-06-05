FROM islandora/claw-tomcat:open-jdk  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
ARG BLAZEGRAPH_VERSION="1.5.1"  
ENV CATALINA_OPTS="${CATALINA_OPTS}
-Dcom.bigdata.rdf.sail.webapp.ConfigParams.propertyFile=${CATALINA_BASE}/webapps/bigdata/WEB-
INF/RWStore.properties"  
RUN curl -o ${CATALINA_BASE}/webapps/bigdata.war \  
-L http://sourceforge.net/projects/bigdata/files/bigdata/${BLAZEGRAPH_VERSION}/bigdata.war/download && \  
mkdir ${CATALINA_BASE}/webapps/bigdata && \  
unzip -o ${CATALINA_BASE}/webapps/bigdata.war -d
${CATALINA_HOME}/webapps/bigdata && \  
rm -rf ${CATALINA_HOME}/webapps/*.war && \  
mkdir /opt/blazegraph && \  
chown tomcat:tomcat /opt/blazegraph && \  
cleanup  
  
COPY rootfs /  

