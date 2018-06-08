FROM tomcat:9.0.0.M9-jre8-alpine  
  
RUN rm -rf /usr/local/tomcat/webapps/ROOT  
  
COPY context.xml /usr/local/tomcat/conf/context.xml  
  
COPY target/SCOPES-ENDPOINT-1.0-SNAPSHOT.war
/usr/local/tomcat/webapps/ROOT.war  
  
EXPOSE 8080  

