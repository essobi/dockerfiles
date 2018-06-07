FROM jetty:latest  
  
ENV INSPECTIT_VERSION 1.8.5.101  
ENV INSPECTIT_AGENT_HOME /opt/agent  
  
# 1. download and unpack agent  
# 2. change owner of agent folder to jetty user to have all permissions  
# 3. define inspectIT start-up options in the /etc/default/jetty (jetty looks
there by default)  
RUN wget
https://github.com/inspectIT/inspectIT/releases/download/${INSPECTIT_VERSION}/inspectit-
agent-java6-${INSPECTIT_VERSION}.zip -q \  
&& unzip inspectit-agent-java6-${INSPECTIT_VERSION}.zip -d /opt \  
&& rm -f inspectit-agent-java6-${INSPECTIT_VERSION}.zip \  
&& chown jetty:jetty -R $INSPECTIT_AGENT_HOME \  
&& echo "JAVA_OPTIONS=(\"-javaagent:${INSPECTIT_AGENT_HOME}/inspectit-
agent.jar\" \"-Dinspectit.repository=_CMR_ADDRESS_:_CMR_PORT_\"
\"-Dinspectit.agent.name=_AGENT_NAME_\")" > /etc/default/jetty  
  
# copy start script  
COPY run-with-inspectit.sh /run-with-inspectit.sh  
  
CMD /run-with-inspectit.sh  

