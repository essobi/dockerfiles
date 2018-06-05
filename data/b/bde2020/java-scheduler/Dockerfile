FROM asjongers/tomcat-java7-maven  
MAINTAINER Vincent Goossens <vincent.goossens@tenforce.com>  
  
ARG VERSION=1.0  
ENV LOG_LEVEL_EU_ESCO="info" LOG_LEVEL_COM_TENFORCE="info"
LOG_LEVEL_ROOT="info"  
ADD settings.xml /root/.m2/settings.xml  
  
ADD . /app  
  
RUN cd /app && mvn install  
  
RUN rm -rf /usr/local/tomcat/webapps/ROOT  
  
RUN mv /app/target/mu-java-scheduler-${VERSION}.war
/usr/local/tomcat/webapps/ROOT.war  
EXPOSE 8080  

