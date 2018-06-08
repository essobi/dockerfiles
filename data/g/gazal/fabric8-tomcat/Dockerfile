FROM jboss/base-jdk:8  
ENV MAVEN_MAJOR 3  
ENV MAVEN_VERSION 3.2.5  
ENV DEPLOY_DIR /opt/jboss/deploy  
LABEL io.s2i.scripts-url https://raw.githubusercontent.com/fabric8io/base-
sti/master/.sti/bin/  
LABEL io.s2i.destination /tmp  
USER root  
  
RUN curl
http://www.apache.org/dist/maven/maven-$MAVEN_MAJOR/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar -xzf - -C /opt/jboss \  
&& mv /opt/jboss/apache-maven-$MAVEN_VERSION /opt/jboss/maven \  
&& mkdir -p /opt/jboss/deploy \  
&& chown -R jboss:jboss /opt/jboss \  
&& chmod -R 755 /opt/jboss/maven/ \  
&& ln -sf /opt/jboss/maven/bin/mvn /usr/local/bin/mvn  
  
# Configure Source-To-Image scripts  
ADD ./bin /usr/bin/  
  
USER jboss  
  
CMD ["/usr/bin/usage"]  
  
EXPOSE 8080 8778  
ENV TOMCAT_VERSION 7.0.62  
ENV DEPLOY_DIR /maven  
  
  
USER root  
# Get and Unpack Tomcat  
RUN curl
http://archive.apache.org/dist/tomcat/tomcat-7/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz | tar -xzf - -C /opt \  
&& ln -s /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat \  
&& chown -R jboss:jboss /opt/tomcat/  
USER jboss  
  
# Add roles  
ADD tomcat-users.xml /opt/apache-tomcat-${TOMCAT_VERSION}/conf/  
  
# Startup script  
ADD deploy-and-run.sh /opt/apache-tomcat-${TOMCAT_VERSION}/bin/  
  
# jolokia agent  
RUN curl http://central.maven.org/maven2/org/jolokia/jolokia-
jvm/1.3.1/jolokia-jvm-1.3.1-agent.jar > /opt/tomcat/jolokia-agent.jar  
  
# Remove unneeded apps  
RUN rm -rf /opt/tomcat/webapps/examples /opt/tomcat/webapps/docs
/opt/tomcat/webapps/ROOT  
  
# VOLUME ["/opt/tomcat/logs", "/opt/tomcat/work", "/opt/tomcat/temp",
"/tmp/hsperfdata_root"  
ENV CATALINA_OPTS -javaagent:/opt/tomcat/jolokia-
agent.jar=host=0.0.0.0,port=8778  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
CMD /opt/tomcat/bin/deploy-and-run.sh  
  

