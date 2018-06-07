FROM domeos/java:jdk8  
  
MAINTAINER domeos  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.26  
ENV CATALINA_HOME=/opt/tomcat  
ENV JAVA_HOME /opt/jdk  
ENV PATH=${CATALINA_HOME}/bin:${PATH}  
  
WORKDIR /opt  
  
RUN curl -ssL
https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -o tomcat.tar.gz && \  
tar -xzf tomcat.tar.gz -C /opt && \  
rm -rf tomcat.tar.gz && \  
mv /opt/apache-tomcat-${TOMCAT_VERSION} ${CATALINA_HOME}  
  
EXPOSE 8080  
EXPOSE 8009  
VOLUME "/opt/tomcat/webapps"  
WORKDIR /opt/tomcat  
  
CMD ["/opt/tomcat/bin/catalina.sh", "run"]  

