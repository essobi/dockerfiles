FROM java:8-jre  
MAINTAINER Alexander Gorokhov <sashgorokhov@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y unzip git  
  
ENV SERVER_URL="" \  
AGENT_OWN_ADDRESS="" \  
AGENT_OWN_PORT="9090" \  
AGENT_NAME="" \  
AGENT_DIR="/opt/teamcity_agent"  
ENV AGENT_WORKDIR=$AGENT_DIR"/work_dir" \  
AGENT_TEMPDIR=$AGENT_DIR"/temp_dir"  
EXPOSE $AGENT_OWN_PORT  
VOLUME $AGENT_WORKDIR $AGENT_TEMPDIR  
WORKDIR $AGENT_DIR  
  
RUN mkdir /agent-init.d  
COPY /setup_docker.sh /agent-init.d/  
  
COPY setup_agent.sh /  
CMD /setup_agent.sh && $AGENT_DIR/bin/agent.sh run  

