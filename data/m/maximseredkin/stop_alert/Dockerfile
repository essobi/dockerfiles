FROM maven:3.5-jdk-8-onbuild  
  
FROM tomcat:9.0.0-jre8  
RUN rm -rf /usr/local/tomcat/webapps/ROOT/  
COPY \--from=0 /usr/src/app/target/app.war /usr/local/tomcat/webapps/ROOT.war

