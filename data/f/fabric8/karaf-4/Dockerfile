FROM jboss/base-jdk:8  
  
MAINTAINER rhuss@redhat.com  
  
EXPOSE 8181 8101  
  
ENV KARAF_VERSION 4.0.5  
  
USER root  
  
# Agent bond including Jolokia and jmx_exporter  
ADD agent-bond-opts /opt/run-java-options  
RUN mkdir -p /opt/agent-bond \  
&& curl http://central.maven.org/maven2/io/fabric8/agent-bond-
agent/0.1.3/agent-bond-agent-0.1.3.jar \  
-o /opt/agent-bond/agent-bond.jar \  
&& chmod 444 /opt/agent-bond/agent-bond.jar \  
&& chmod 755 /opt/run-java-options  
ADD jmx_exporter_config.yml /opt/agent-bond/  
EXPOSE 8778 9779  
  
  
RUN curl http://archive.apache.org/dist/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.tar.gz -o /tmp/karaf.tar.gz \  
&& tar xzf /tmp/karaf.tar.gz -C /opt/ \  
&& ln -s /opt/apache-karaf-${KARAF_VERSION} /opt/karaf \  
&& chown -R jboss /opt/karaf /opt/apache-karaf-${KARAF_VERSION} \  
&& rm /tmp/karaf.tar.gz  
  
# Add roles  
ADD users.properties /opt/apache-karaf-${KARAF_VERSION}/etc/  
  
# Startup script  
ADD deploy-and-run.sh /opt/karaf/bin/  
  
RUN chmod a+x /opt/karaf/bin/deploy-and-run.sh \  
&& rm -rf /opt/karaf/deploy/README \  
&& sed -i 's/^\\(.*rootLogger.*\\)out/\1stdout/'
/opt/karaf/etc/org.ops4j.pax.logging.cfg  
  
# Add debug-options and java-container-options to /opt and make it executable  
COPY debug-options java-container-options /opt/  
RUN chmod 755 /opt/debug-options /opt/java-container-options  
  
  
ENV PATH $PATH:/opt/karaf/bin  
  
CMD /opt/karaf/bin/deploy-and-run.sh  
  
USER jboss  

