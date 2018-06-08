FROM dockerfile/java:oracle-java8  
  
EXPOSE 8080 8081  
ENV TOMCAT_VERSION 8.0.12  
RUN wget --quiet --no-cookies
http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/catalina.tar.gz  
  
# Unpack  
RUN tar xzf /tmp/catalina.tar.gz -C /opt  
RUN mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat  
RUN rm /tmp/catalina.tar.gz  
  
ADD tomcat-users.xml /opt/tomcat/conf/  
ADD catalina2.sh /opt/tomcat/bin/  
ADD startup2.sh /opt/tomcat/bin/  
  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
RUN chmod +rwx /opt/tomcat/bin/catalina2.sh  
RUN chmod +rwx /opt/tomcat/bin/startup2.sh  
  
CMD ["/opt/tomcat/bin/catalina2.sh", "run"]

