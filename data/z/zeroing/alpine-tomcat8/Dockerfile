FROM zeroing/alpine-oraclejre8:3.7_8u161-b12  
  
MAINTAINER zeroing <admin@zeroing.io>  
  
EXPOSE 8080  
ENV TOMCAT_VERSION 8.0.36  
ENV DEPLOY_DIR /maven  
  
USER root  
  
# Agent bond including Jolokia and jmx_exporter  
ADD jmx-opts /opt/run-java-options  
RUN mkdir -p /opt/monitor \  
&& apk add --no-cache --virtual=build-dependencies curl \  
&& curl http://search.maven.org/remotecontent?filepath=org/jolokia/jolokia-
jvm/1.5.0/jolokia-jvm-1.5.0-agent.jar \  
-o /opt/monitor/jolokia-jvm-agent.jar \  
&& curl
https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.3.0/jmx_prometheus_javaagent-0.3.0.jar
\  
-o /opt/monitor/jmx_prometheus_javaagent.jar \  
&& chmod 444 /opt/monitor/jolokia-jvm-agent.jar \  
&& chmod 444 /opt/monitor/jmx_prometheus_javaagent.jar \  
&& chmod 755 /opt/run-java-options  
ADD jmx_exporter_config.yml /opt/monitor/  
EXPOSE 8778 9779  
# Get and Unpack Tomcat  
RUN curl
http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -o /tmp/catalina.tar.gz \  
&& tar xzf /tmp/catalina.tar.gz -C /opt \  
&& ln -s /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat \  
&& rm /tmp/catalina.tar.gz  
  
# Startup script  
ADD deploy-and-run.sh /opt/apache-tomcat-${TOMCAT_VERSION}/bin/  
  
RUN chmod 755 /opt/apache-tomcat-${TOMCAT_VERSION}/bin/deploy-and-run.sh \  
&& rm -rf /opt/tomcat/webapps/*  
  
VOLUME [ "/opt/tomcat/logs", "/opt/tomcat/work", "/opt/tomcat/temp",
"/tmp/hsperfdata_root" ]  
  
# Add java-container-options to /opt and make it executable  
COPY java-container-options /opt/  
RUN chmod 755 /opt/java-container-options  
  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
CMD /opt/tomcat/bin/deploy-and-run.sh  

