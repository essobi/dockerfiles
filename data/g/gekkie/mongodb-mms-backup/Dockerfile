###  
#  
# A simple image for installing the mongodb-mms-backup-agent  
#  
###  
FROM gekkie/mongodb-mms-agent-base:0.1  
MAINTAINER Kingsquare <docker@kingsquare.nl>  
  
####  
# Install Agent itself  
RUN curl -sSL https://mms.mongodb.com/download/agent/backup/mongodb-mms-
backup-agent_2.8.0.204-1_amd64.deb -o mms.deb && \  
dpkg -i mms.deb && \  
rm mms.deb  
  
USER mongodb-mms-agent  
CMD ["mongodb-mms-backup-agent", "-c", "/etc/mongodb-mms/backup-agent.config"]

