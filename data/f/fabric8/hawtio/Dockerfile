FROM fabric8/tomcat-8.0  
MAINTAINER fabric8@googlegroups.com  
  
ENV FABRIC8_VERSION 2.0.25  
ENV HAWTIO_VERSION 1.4.47  
ENV HAWTIO_SWAGGER_VERSION 1.0.2  
ENV JOLOKIA_DISABLE true  
  
# configuring what initial repository to configure on startup  
#ENV hawtio_config_repo  
# should we clone the remote repo on startup?  
ENV hawtio_config_cloneOnStartup false  
  
# which initial maven URLs (comma separated) should be imported into the
default application library  
ENV hawtio_config_importURLs mvn:io.fabric8.quickstarts/fabric8-quickstarts-
parent/$FABRIC8_VERSION/zip/app,mvn:io.fabric8.jube.images.fabric8/apps/$FABRIC8_VERSION/zip/app  
  
RUN rm -rf /opt/tomcat/webapps/*; mkdir /opt/tomcat/webapps/ROOT; wget
http://central.maven.org/maven2/io/fabric8/console/$FABRIC8_VERSION/console-$FABRIC8_VERSION.war
-qO /opt/tomcat/webapps/hawtio.war; wget
http://central.maven.org/maven2/io/hawt/swagger/hawtio-swagger-
ui/$HAWTIO_SWAGGER_VERSION/hawtio-swagger-ui-$HAWTIO_SWAGGER_VERSION.war -qO
/opt/tomcat/webapps/hawtio-swagger.war  
  
ADD index.html /opt/tomcat/webapps/ROOT/index.html  
  
ADD logging.properties /opt/tomcat/conf/logging.properties  
  
CMD /opt/tomcat/bin/catalina.sh run  

