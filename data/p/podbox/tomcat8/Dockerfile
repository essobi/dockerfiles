FROM podbox/java8  
  
# ----------------------------------------------------------------------
tomcat8  
ENV TOMCAT_VERSION 8.0.33  
RUN (curl -L
http://www.us.apache.org/dist/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz | gunzip -c | tar x) \  
&& mv apache-tomcat-$TOMCAT_VERSION /apache-tomcat \  
&& rm -fR /apache-tomcat/webapps/*  
  
RUN cd /apache-tomcat/conf \  
&& echo '\njava.awt.headless=true' >> catalina.properties  
  
RUN cd /apache-tomcat/lib \  
&& curl -LO https://jcenter.bintray.com/org/apache/openejb/tomee-
loader/1.7.3/tomee-loader-1.7.3.jar \  
&& curl -LO
https://jcenter.bintray.com/org/glassfish/main/external/jmxremote_optional-
repackaged/4.1.1/jmxremote_optional-repackaged-4.1.1.jar  
  
ADD server.xml /apache-tomcat/conf/  
ADD context.xml /apache-tomcat/conf/  
  
EXPOSE 8080 9875  
CMD ["/apache-tomcat/bin/catalina.sh", "run"]  

