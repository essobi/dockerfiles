###  
#  
# A simple image for installing the mongodb-mms-backup-agent  
#  
###  
FROM gekkie/mongodb-mms-agent-base:0.2  
MAINTAINER Kingsquare <docker@kingsquare.nl>  
  
####  
# Install Agent itself  
RUN curl -sSL https://mms.mongodb.com/download/agent/monitoring/mongodb-mms-
monitoring-agent_4.1.0.251-1_amd64.deb -o mms.deb && \  
dpkg -i mms.deb && \  
rm mms.deb  
  
USER mongodb-mms-agent  
CMD ["mongodb-mms-monitoring-agent", "-conf", "/etc/mongodb-mms/monitoring-
agent.config"]  

