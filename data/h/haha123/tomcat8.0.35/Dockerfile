FROM undancer/jdk8  
  
MAINTAINER lijiapengas@gmail.com  
  
ENV TOMCAT_VERSION 8.0.35  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
ADD http://apache.rediris.es/tomcat/tomcat-8/v8.0.35/bin/apache-
tomcat-8.0.35.tar.gz /  
  
RUN \  
tar xzvf /apache-tomcat-${TOMCAT_VERSION}.tar.gz -C /opt && \  
mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat && \  
rm -rf /opt/tomcat/*  
  
VOLUME "/opt/tomcat"  
  
EXPOSE 8080  
EXPOSE 8009  
CMD ["/opt/tomcat/bin/catalina.sh", "run"]  
  

