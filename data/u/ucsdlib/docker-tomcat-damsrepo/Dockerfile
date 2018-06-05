# Multistage build  
# We need to build damsrepo first and then copy the war to tomcat  
FROM openjdk:8 as damsrepo-builder  
MAINTAINER "Matt Critchlow <mcritchlow@ucsd.edu">  
  
RUN apt-get update && apt-get install -y git ant  
RUN git clone https://github.com/ucsdlib/damsrepo.git /tmp/damsrepo  
WORKDIR /tmp/damsrepo  
RUN ant webapp  
RUN mkdir -p /pub/dams  
RUN mv /tmp/damsrepo/dist/dams.war /pub/dams/  
RUN mv /tmp/damsrepo/src/properties/jhove.conf /pub/dams/  
RUN mv /tmp/damsrepo/src/lib2/postgresql-9.2-1002.jdbc4.jar /pub/dams/  
  
FROM tomcat:7-jre8  
MAINTAINER "Matt Critchlow <mcritchlow@ucsd.edu">  
  
# Environment defaults. Obviously, uh, *development*  
ENV MANAGER_USER tomcat  
ENV MANAGER_PASS tomcat  
ENV DAMS_USER dams  
ENV DAMS_PASS dams  
  
  
# setup config and other required files  
COPY tomcat/tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml  
COPY tomcat/server.xml /usr/local/tomcat/conf/server.xml  
  
# Install solr  
COPY solr /usr/local/tomcat/solr/  
ADD solr.war /usr/local/tomcat/webapps/  
  
# Install damsrepo and friends  
RUN mkdir -p /pub/dams/editBackups  
RUN mkdir -p /pub/dams/xsl  
COPY damsrepo/xsl /pub/dams/xsl/  
COPY damsrepo/dams.properties /pub/dams/dams.properties  
COPY \--from=damsrepo-builder /pub/dams/jhove.conf /pub/dams/jhove.conf  
COPY \--from=damsrepo-builder /pub/dams/postgresql-9.2-1002.jdbc4.jar
/usr/local/tomcat/lib/postgresql-9.2-1002.jdbc4.jar  
COPY \--from=damsrepo-builder /pub/dams/dams.war /usr/local/tomcat/webapps/  

