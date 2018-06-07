FROM tutum/jboss:as5  
MAINTAINER info.inspectit@novatec-gmbh.de  
  
# set Workdir  
WORKDIR /opt  
  
# set insepctit env  
ENV INSPECTIT_VERSION 1.8.5.101  
ENV INSPECTIT_AGENT_HOME /opt/agent  
  
# get inspectit binary  
# set inspectit jvm options  
RUN wget --no-check-certificate
https://github.com/inspectIT/inspectIT/releases/download/${INSPECTIT_VERSION}/inspectit-
agent-java6-${INSPECTIT_VERSION}.zip \  
&& unzip inspectit-agent-java6-${INSPECTIT_VERSION}.zip \  
&& rm -f inspectit-agent-java6-${INSPECTIT_VERSION}.zip \  
&& sed -i '$ a\'"export
INSPECTIT_JAVA_OPTS=\"-javaagent:${INSPECTIT_AGENT_HOME}/inspectit-agent.jar
-Dinspectit.repository=_CMR_ADDRESS_:_CMR_PORT_
-Dinspectit.agent.name=_AGENT_NAME_\"" /jboss-5.1.0.GA/bin/run.conf \  
&& sed -i '$ a\'"export JAVA_OPTS=\"\${INSPECTIT_JAVA_OPTS} \${JAVA_OPTS}\""
/jboss-5.1.0.GA/bin/run.conf  
  
# copy start script  
COPY run-with-inspectit.sh /run-with-inspectit.sh  
  
# define default command  
CMD ["/run-with-inspectit.sh"]  

