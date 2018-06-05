FROM tomcat:7.0.81-jre8  
MAINTAINER Jeremie Lesage <jeremie.lesage@gmail.com>  
  
ENV NEXUS=https://artifacts.alfresco.com/nexus/content/groups/public  
  
WORKDIR /usr/local/tomcat/  
  
ENV ALF_VERSION=5.1.g  
  
## SOLR.WAR  
RUN set -x && \  
curl --silent --location \  
${NEXUS}/org/alfresco/alfresco-solr4/${ALF_VERSION}/alfresco-
solr4-${ALF_VERSION}.war \  
-o alfresco-solr4-${ALF_VERSION}.war && \  
unzip -q alfresco-solr4-${ALF_VERSION}.war -d webapps/solr4 && \  
rm alfresco-solr4-${ALF_VERSION}.war  
  
COPY assets/web.xml webapps/solr4/WEB-INF/web.xml  
  
## SOLR CONF  
RUN set -x && \  
curl --silent --location \  
${NEXUS}/org/alfresco/alfresco-solr4/${ALF_VERSION}/alfresco-
solr4-${ALF_VERSION}-config.zip \  
-o alfresco-solr4-${ALF_VERSION}-config.zip && \  
unzip -q alfresco-solr4-${ALF_VERSION}-config.zip -d /opt/solr/ && \  
rm alfresco-solr4-${ALF_VERSION}-config.zip  
  
COPY assets/workspace/* /opt/solr/workspace-SpacesStore/conf/  
COPY assets/archive/* /opt/solr/archive-SpacesStore/conf/  
  
RUN mkdir /opt/solr_data/ \  
&& rm -rf /usr/share/doc \  
webapps/docs \  
webapps/examples \  
webapps/manager \  
webapps/host-manager  
  
ENV JAVA_OPTS " -XX:-DisableExplicitGC -Djava.security.egd=file:/dev/./urandom
-Djava.awt.headless=true -Dfile.encoding=UTF-8 "  
VOLUME "/opt/solr_data/"  
WORKDIR /root  

