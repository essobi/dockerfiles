FROM jboss/base-jdk:8  
MAINTAINER rhuss@redhat.com  
  
EXPOSE 8080  
ENV JETTY_VERSION 9.4.9.v20180320  
ENV DEPLOY_DIR /deployments  
ENV JAVA /usr/bin/java  
  
USER root  
  
# Agent bond including Jolokia and jmx_exporter  
ADD agent-bond-opts /opt/run-java-options  
RUN mkdir -p /opt/agent-bond \  
&& curl http://central.maven.org/maven2/io/fabric8/agent-bond-
agent/1.2.0/agent-bond-agent-1.2.0.jar \  
-o /opt/agent-bond/agent-bond.jar \  
&& chmod 444 /opt/agent-bond/agent-bond.jar \  
&& chmod 755 /opt/run-java-options  
ADD jmx_exporter_config.yml /opt/agent-bond/  
EXPOSE 8778 9779  
RUN curl http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/${JETTY_VERSION}/jetty-distribution-${JETTY_VERSION}.tar.gz -o
/tmp/jetty.tar.gz \  
&& cd /opt && tar zxvf /tmp/jetty.tar.gz \  
&& ln -s /opt/jetty-distribution-${JETTY_VERSION} /opt/jetty \  
&& chown -R jboss /opt/jetty /opt/jetty-distribution-${JETTY_VERSION} \  
&& usermod -g root -G jboss jboss \  
&& chmod -R "g+rwX" /opt/jetty /opt/jetty-distribution-${JETTY_VERSION} \  
&& chown -R jboss:root /opt/jetty /opt/jetty-distribution-${JETTY_VERSION} \  
&& rm /tmp/jetty.tar.gz  
  
# Startup script & permissions for OpenShift  
ADD deploy-and-run.sh /opt/jetty/bin/  
ADD jetty-logging.xml /opt/jetty/etc/  
RUN chmod a+x /opt/jetty/bin/deploy-and-run.sh  
  
# Add run script as /opt/run-java.sh and make it executable  
COPY run-java.sh /opt/  
RUN chmod 755 /opt/run-java.sh  
  
ENV JETTY_HOME /opt/jetty  
ENV PATH $PATH:$JETTY_HOME/bin  
  
CMD /opt/jetty/bin/deploy-and-run.sh  
  
USER jboss  

