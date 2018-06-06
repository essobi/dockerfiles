FROM islandora/claw-tomcat:open-jdk  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
EXPOSE 61613  
EXPOSE 61616  
ARG FEDORA_VERSION="4.4.0"  
ENV FEDORA_HOME="/mnt/fedora-data" \  
CATALINA_OPTS="${CATALINA_OPTS} -Dfcrepo.home=/mnt/fedora-data"  
RUN mkdir -p ${FEDORA_HOME} && \  
chown tomcat:tomcat ${FEDORA_HOME} && \  
curl -o ${CATALINA_BASE}/webapps/fcrepo.war \  
-L https://github.com/fcrepo4/fcrepo4/releases/download/fcrepo-${FEDORA_VERSION}/fcrepo-webapp-${FEDORA_VERSION}.war && \  
mkdir ${CATALINA_BASE}/webapps/fcrepo && \  
unzip -o ${CATALINA_BASE}/webapps/fcrepo.war -d
${CATALINA_HOME}/webapps/fcrepo && \  
rm -rf ${CATALINA_HOME}/webapps/*.war && \  
cleanup  
  
COPY rootfs /  

