FROM tomcat  
MAINTAINER info.inspectit@novatec-gmbh.de  
  
# set Workdir  
WORKDIR /opt  
  
# set insepctit env options  
ENV INSPECTIT_VERSION 1.8.5.101  
ENV INSPECTIT_AGENT_HOME /opt/agent  
  
# get inspectit binary  
# set inspectit jvm options  
RUN wget --no-check-certificate
https://github.com/inspectIT/inspectIT/releases/download/${INSPECTIT_VERSION}/inspectit-
agent-java6-${INSPECTIT_VERSION}.zip \  
&& unzip inspectit-agent-java6-${INSPECTIT_VERSION}.zip \  
&& rm -f inspectit-agent-java6-${INSPECTIT_VERSION}.zip \  
&& sed -i '250i\'"export
INSPECTIT_JAVA_OPTS=\"-javaagent:${INSPECTIT_AGENT_HOME}/inspectit-agent.jar
-Dinspectit.repository=_CMR_ADDRESS_:_CMR_PORT_
-Dinspectit.agent.name=_AGENT_NAME_\"" /usr/local/tomcat/bin/catalina.sh \  
&& sed -i '251i\'"export JAVA_OPTS=\"\${INSPECTIT_JAVA_OPTS} \${JAVA_OPTS}\""
/usr/local/tomcat/bin/catalina.sh  
  
# copy start script  
COPY run-with-inspectit.sh /run-with-inspectit.sh  
  
# define default command  
CMD ["/run-with-inspectit.sh", "run"]  

