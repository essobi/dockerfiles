FROM fufler/tomcat:7-jre8  
MAINTAINER Alexey Ermakov <fufler@gmail.com>  
  
  
ENV ARTIFACTS_REPO_BASE
https://artifacts.alfresco.com/nexus/service/local/repo_groups/public/content/  
ENV GITHUB_BASE_URL https://github.com  
  
# ENV ARTIFACTS_REPO_BASE
http://proxy:8000/nexus/service/local/repo_groups/public/content/  
# ENV GITHUB_BASE_URL http://proxy:8000/  
ENV PGSQL_PORT 5432  
RUN apt-get update -qq && apt-get -qq install --no-install-recommends
libreoffice ghostscript imagemagick && apt-get -qq clean  
  
ENV ALF_AMPS_TARGETS platform  
  
ENV ALF_VERSION 5.2.a-EA  
ENV PG_JDBC_VERSION 9.2-1002.jdbc4  
ENV JS_CONSOLE_VERSION 0.6.0  
ENV JS_CONSOLE_RC -rc1  
  
ENV ALF_REPO_LINK
${ARTIFACTS_REPO_BASE}/org/alfresco/alfresco/${ALF_VERSION}/alfresco-${ALF_VERSION}.war  
ENV ALF_SOLR4_LINK ${ARTIFACTS_REPO_BASE}/org/alfresco/alfresco-
solr4/${ALF_VERSION}/alfresco-solr4-${ALF_VERSION}.war  
ENV ALF_AMP_SHARE_SERVICES_LINK ${ARTIFACTS_REPO_BASE}/org/alfresco/alfresco-
share-services/${ALF_VERSION}/alfresco-share-services-${ALF_VERSION}.amp  
ENV ALF_JAR_MMT_LINK ${ARTIFACTS_REPO_BASE}/org/alfresco/alfresco-
mmt/${ALF_VERSION}/alfresco-mmt-${ALF_VERSION}.jar  
ENV ALF_JAR_PG_JDBC
${ARTIFACTS_REPO_BASE}/postgresql/postgresql/${PG_JDBC_VERSION}/postgresql-${PG_JDBC_VERSION}.jar  
ENV ALF_AMP_JS_CONSOLE_LINK ${GITHUB_BASE_URL}/share-extras/js-
console/releases/download/v${JS_CONSOLE_VERSION}${JS_CONSOLE_RC}/javascript-
console-repo-${JS_CONSOLE_VERSION}.amp  
  
ENV MMT_JAR_PATH /usr/local/tomcat/bin/alfresco-mmt.jar  
  
RUN mkdir /usr/local/tomcat/alf_data  
COPY conf /usr/local/tomcat/conf/  
COPY shared /usr/local/tomcat/shared/  
COPY solr4 /usr/local/tomcat/solr4/  
  
VOLUME /usr/local/tomcat/alf_data  
  
ADD ${ALF_REPO_LINK} /usr/local/tomcat/webapps/alfresco.war  
ADD ${ALF_SOLR4_LINK} /usr/local/tomcat/webapps/solr4.war  
ADD ${ALF_AMP_SHARE_SERVICES_LINK} /usr/local/tomcat/amps/alfresco-share-
services.amp  
ADD ${ALF_AMP_JS_CONSOLE_LINK} /usr/local/tomcat/amps/  
ADD ${ALF_JAR_MMT_LINK} ${MMT_JAR_PATH}  
ADD ${ALF_JAR_PG_JDBC} /usr/local/tomcat/lib/  
  
EXPOSE 8080 8443  

