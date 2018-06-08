# Ubuntu 14.04 LTS  
# Oracle Java 1.8 64 bit  
# extend the most recent long term support Ubuntu version  
FROM plopezmesa/java8  
  
MAINTAINER Pablo López Mesa (plopezmesa@gmail.com)  
  
# this is a non-interactive automated build - avoid some warning messages  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TOMCAT_VERSION 8.0.24  
ENV CATALINA_HOME /apache-tomcat  
  
  
RUN wget --quiet --no-cookies
http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/catalina.tar.gz  
  
# Unpack  
RUN tar xzf /tmp/catalina.tar.gz -C /tmp  
RUN mv /tmp/apache-tomcat-${TOMCAT_VERSION} $CATALINA_HOME  
RUN rm /tmp/catalina.tar.gz  
  
# Remove unneeded apps  
RUN rm -rf $CATALINA_HOME/webapps/examples  
RUN rm -rf $CATALINA_HOME/webapps/docs  
RUN rm -rf $CATALINA_HOME/webapps/ROOT  
  
ADD tomcat-users.xml $CATALINA_HOME/conf/  
  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
EXPOSE 8080  
EXPOSE 8009  
# Start Tomcat  
CMD ["/apache-tomcat/bin/catalina.sh", "run"]  
  

