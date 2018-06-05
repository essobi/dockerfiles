FROM tomcat:7.0.81-jre8  
MAINTAINER Jeremie Lesage <jeremie.lesage@gmail.com>  
  
ENV NEXUS=https://artifacts.alfresco.com/nexus/content/groups/public  
  
WORKDIR /usr/local/tomcat/  
  
ENV MMT_VERSION=5.1.g  
  
## JAR - ALFRESCO MMT  
RUN set -x && \  
curl --silent --location \  
${NEXUS}/org/alfresco/alfresco-mmt/${MMT_VERSION}/alfresco-
mmt-${MMT_VERSION}.jar \  
-o /root/alfresco-mmt.jar && \  
mkdir /root/amp  
  
ENV ALF_VERSION=5.1.g  
  
## SHARE.WAR  
RUN set -x && \  
curl --silent --location \  
${NEXUS}/org/alfresco/share/${ALF_VERSION}/share-${ALF_VERSION}.war \  
-o share-${ALF_VERSION}.war && \  
unzip -q share-${ALF_VERSION}.war -d webapps/share && \  
rm share-${ALF_VERSION}.war  
  
RUN set -x \  
&& sed -i 's/^log4j.rootLogger.*/log4j.rootLogger=error, Console/'
webapps/share/WEB-INF/classes/log4j.properties \  
&& mkdir -p shared/classes/alfresco/web-extension \  
shared/lib \  
&& rm -rf /usr/share/doc \  
webapps/docs \  
webapps/examples \  
webapps/manager \  
webapps/host-manager  
  
COPY assets/catalina.properties conf/catalina.properties  
COPY assets/share-config-custom.xml shared/classes/alfresco/web-
extension/share-config-custom.xml  
COPY assets/server.xml conf/server.xml  
COPY assets/logging.properties conf/logging.properties  
  
ENV JAVA_OPTS " -XX:-DisableExplicitGC -Djava.security.egd=file:/dev/./urandom
-Djava.awt.headless=true -Dfile.encoding=UTF-8 "  
WORKDIR /root  

