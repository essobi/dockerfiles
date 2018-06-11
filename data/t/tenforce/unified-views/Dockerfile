FROM tomcat:7-jre8  
  
MAINTAINER Bert Van Nuffelen <Bert.Van.Nuffelen@tenforce.com>  
  
  
# libs  
ADD
https://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/backend-
libs/3.0.0/backend-libs-3.0.0.zip /unified-views/lib/backend-libs-3.0.0.zip  
ADD
https://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/dpu-v2-compatibility-
package/1.0.0/dpu-v2-compatibility-package-1.0.0.jar /unified-
views/lib/dpu-v2-compatibility-package-1.0.0.jar  
RUN cd /unified-views/lib && unzip backend-libs-3.0.0.zip  
# backend  
ADD
http://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/backend/3.0.0/backend-3.0.0.jar
/unified-views/backend.jar  
  
# frontend  
ADD
http://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/master/3.0.0/master-3.0.0.war
/usr/local/tomcat/webapps/master-3.0.0.war  
ADD
http://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/frontend/3.0.0/frontend-3.0.0.war
/usr/local/tomcat/webapps/unifiedviews-3.0.0.war  
  
ADD config /config  
  
WORKDIR /unified-views  
  
EXPOSE 8080  
EXPOSE 8066  
EXPOSE 5001  
  
RUN chmod +x /config/*.sh && chmod -R 777 /config  
  
  
CMD ["/config/start.sh", ""]  

