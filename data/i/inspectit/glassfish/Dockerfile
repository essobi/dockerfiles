FROM glassfish:latest  
  
ENV INSPECTIT_VERSION 1.8.5.101  
ENV INSPECTIT_AGENT_HOME /opt/agent  
  
# download agent and prepare  
RUN wget
https://github.com/inspectIT/inspectIT/releases/download/${INSPECTIT_VERSION}/inspectit-
agent-java6-${INSPECTIT_VERSION}.zip -q \  
&& unzip inspectit-agent-java6-${INSPECTIT_VERSION}.zip -d /opt \  
&& apt-get clean \  
&& rm -rf /var/lib/apt \  
&& rm -f inspectit-agent-java6-${INSPECTIT_VERSION}.zip  
  
# alter the configuration for the domain to include inspectIT options  
RUN sed -i "s#\(</java-config>\)#<jvm-
options>-javaagent:\${INSPECTIT_AGENT_HOME}/inspectit-agent.jar</jvm-
options>\1#" glassfish/domains/domain1/config/domain.xml \  
&& sed -i "s#\(</java-config>\)#<jvm-
options>-Dinspectit.repository=_CMR_ADDR_:_CMR_PORT_</jvm-options>\1#"
glassfish/domains/domain1/config/domain.xml \  
&& sed -i "s#\(</java-config>\)#<jvm-
options>-Dinspectit.agent.name=_AGENT_NAME_</jvm-options>\1#"
glassfish/domains/domain1/config/domain.xml \  
&& sed -i "s/org\.netbeans\.lib\.profiler,
org\.netbeans\.lib\.profiler.*/org\.netbeans\.lib\.profiler,
org\.netbeans\.lib\.profiler\.\*, rocks\.inspectit\.\*/"
glassfish/config/osgi.properties  
  
# copy start script  
COPY run-with-inspectit.sh /run-with-inspectit.sh  
  
CMD /run-with-inspectit.sh  

