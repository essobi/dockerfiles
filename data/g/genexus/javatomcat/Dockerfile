  
FROM tomcat:8.5-jre8-alpine  
  
LABEL com.genexus.name="GeneXus Java Tomcat for Linux" \  
com.genexus.description="GeneXus Dockerfile for Java Tomcat environments" \  
com.genexus.url="http://www.genexus.com/" \  
com.genexus.vcs-url="https://github.com/genexuslabs/dockerfiles" \  
com.genexus.vendor="GeneXus" \  
com.genexus.schema-version="1.0" \  
com.genexus.maintainer="Seba Gómez <sgomez@genexus.com>"  
  
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml  
COPY manager.xml /usr/local/tomcat/conf/Catalina/localhost/manager.xml  

