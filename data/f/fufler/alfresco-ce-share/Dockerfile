FROM fufler/tomcat:7-jre8  
MAINTAINER Alexey Ermakov <fufler@gmail.com>  
  
  
ENV ARTIFACTS_REPO_BASE
https://artifacts.alfresco.com/nexus/service/local/repo_groups/public/content/  
ENV GITHUB_BASE_URL https://github.com  
  
# ENV ARTIFACTS_REPO_BASE
http://proxy:8000/nexus/service/local/repo_groups/public/content/  
# ENV GITHUB_BASE_URL http://proxy:8000/  
ENV REPO_PORT 8080  
ENV ALF_AMPS_TARGETS share  
  
ENV ALF_VERSION 5.2.a-EA  
ENV JS_CONSOLE_VERSION 0.6.0  
ENV JS_CONSOLE_RC -rc1  
  
ENV ALF_SHARE_LINK
${ARTIFACTS_REPO_BASE}/org/alfresco/share/${ALF_VERSION}/share-${ALF_VERSION}.war  
ENV ALF_AMP_SHARE_SERVICES_LINK ${ARTIFACTS_REPO_BASE}/org/alfresco/alfresco-
share-services/${ALF_VERSION}/alfresco-share-services-${ALF_VERSION}.amp  
ENV ALF_JAR_MMT_LINK ${ARTIFACTS_REPO_BASE}/org/alfresco/alfresco-
mmt/${ALF_VERSION}/alfresco-mmt-${ALF_VERSION}.jar  
ENV ALF_AMP_JS_CONSOLE_LINK ${GITHUB_BASE_URL}/share-extras/js-
console/releases/download/v${JS_CONSOLE_VERSION}${JS_CONSOLE_RC}/javascript-
console-share-${JS_CONSOLE_VERSION}.amp  
  
ENV MMT_JAR_PATH /usr/local/tomcat/bin/alfresco-mmt.jar  
  
COPY conf /usr/local/tomcat/conf/  
COPY shared /usr/local/tomcat/shared/  
  
ADD ${ALF_SHARE_LINK} /usr/local/tomcat/webapps/share.war  
ADD ${ALF_AMP_JS_CONSOLE_LINK} /usr/local/tomcat/amps_share/  
ADD ${ALF_JAR_MMT_LINK} ${MMT_JAR_PATH}  
  
EXPOSE 8080 8443  

