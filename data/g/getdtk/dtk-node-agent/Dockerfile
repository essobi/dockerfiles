FROM ubuntu:14.04  
MAINTAINER dduvnjak <dario@atlantbh.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY . /usr/share/dtk/dtk-node-agent  
  
RUN /usr/share/dtk/dtk-node-agent/install_agent.sh --no-arbiter && \  
mkdir /etc/dtk && \  
mkdir /root/.ssh && \  
chmod 700 /root/.ssh  
  

