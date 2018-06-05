FROM tomcat  
  
COPY logging.properties /usr/local/tomcat/conf/logging.properties  
  
RUN rm -rf /usr/local/tomcat/webapps/*  
ADD http://search.maven.org/remotecontent?filepath=org/jolokia/jolokia-
war/1.3.3/jolokia-war-1.3.3.war /usr/local/tomcat/webapps/jolokia.war  

