FROM ubuntu:12.04  
MAINTAINER Dataloop <info@dataloop.io>  
  
RUN apt-get update && apt-get install -y apt-transport-https  
  
# Install the Agent  
RUN echo 'deb https://download.dataloop.io/deb/ unstable main' >
/etc/apt/sources.list.d/dataloop.list  
ADD https://download.dataloop.io/pubkey.gpg /pubkey.gpg  
RUN apt-key add pubkey.gpg && apt-get update && apt-get install -y dataloop-
agent  
ADD agent.yaml /etc/dataloop/agent.yaml  
  
# Start the Agent  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/dataloop-agent", "--config", "/etc/dataloop/agent.yaml"]  

