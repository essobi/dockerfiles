FROM tomcat:7.0.77-jre8  
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
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
imagemagick \  
ghostscript \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV ALF_VERSION=5.1.g \  
ALF_SHARE_SERVICE=5.1.g  
  
## ALFRESCO.WAR  
RUN set -x && \  
curl --silent --location \  
${NEXUS}/org/alfresco/alfresco-platform/${ALF_VERSION}/alfresco-
platform-${ALF_VERSION}.war \  
-o alfresco-platform-${ALF_VERSION}.war && \  
unzip -q alfresco-platform-${ALF_VERSION}.war -d webapps/alfresco && \  
rm alfresco-platform-${ALF_VERSION}.war  
  
## JDBC - POSTGRESQL  
ENV PG_LIB_VERSION=9.2-1002.jdbc4  
RUN set -x && \  
curl --silent --location \  
${NEXUS}/postgresql/postgresql/${PG_LIB_VERSION}/postgresql-${PG_LIB_VERSION}.jar
\  
-o lib/postgresql-${PG_LIB_VERSION}.jar  
  
## AMP - ALFRESCO SHARE SERVICE  
RUN set -x && \  
curl --silent --location \  
${NEXUS}/org/alfresco/alfresco-share-services/${ALF_SHARE_SERVICE}/alfresco-
share-services-${ALF_SHARE_SERVICE}.amp \  
-o /root/amp/alfresco-share-services-${ALF_SHARE_SERVICE}.amp && \  
java -jar /root/alfresco-mmt.jar install /root/amp/ webapps/alfresco -nobackup
-directory && \  
rm /root/amp/alfresco-share-services-${ALF_SHARE_SERVICE}.amp  
  
RUN set -x && \  
sed -i
's|^log4j.appender.File.File=.*$|log4j.appender.File.File=/usr/local/tomcat/logs/alfresco.log|'
webapps/alfresco/WEB-INF/classes/log4j.properties && \  
mkdir -p shared/classes/alfresco/extension \  
shared/classes/alfresco/messages \  
shared/lib \  
&& rm -rf /usr/share/doc \  
webapps/docs \  
webapps/examples \  
webapps/manager \  
webapps/host-manager  
  
COPY assets/catalina.properties conf/catalina.properties  
COPY assets/server.xml conf/server.xml  
COPY assets/web.xml webapps/alfresco/WEB-INF/web.xml  
COPY assets/alfresco-global.properties webapps/alfresco/WEB-
INF/classes/alfresco-global.properties  
  
ENV JAVA_OPTS: " -XX:-DisableExplicitGC
-Djava.security.egd=file:/dev/./urandom -Djava.awt.headless=true
-Dfile.encoding=UTF-8 "  
WORKDIR /root  
  
VOLUME "/opt/alf_data/"  

