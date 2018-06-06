FROM damm/java8  
  
MAINTAINER juha.komulainen@evident.fi  
  
EXPOSE 8080  
ENV TOMCAT_VERSION 8.0.12  
RUN wget --quiet --no-cookies
http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/catalina.tar.gz  
  
# Unpack  
RUN tar xzf /tmp/catalina.tar.gz -C /opt  
RUN mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat  
RUN rm /tmp/catalina.tar.gz  
  
# Remove unneeded apps  
RUN rm -rf /opt/tomcat/webapps/examples  
RUN rm -rf /opt/tomcat/webapps/docs  
RUN rm -rf /opt/tomcat/webapps/ROOT  
  
ADD tomcat-users.xml /opt/tomcat/conf/  
  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
# Start Tomcat  
CMD ["/opt/tomcat/bin/catalina.sh", "run"]  

