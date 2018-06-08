#  
# MMS Automation Agent Dockerfile  
#  
# https://github.com/eduardocardoso/mms-agent  
#  
# Base image  
FROM phusion/baseimage  
  
CMD ["/sbin/my_init"]  
  
VOLUME ["/data"]  
  
# Install dependencies  
RUN apt-get update && apt-get install -y ca-certificates libsasl2-2  
  
RUN curl -L -o /tmp/mongodb-mms-automation-agent-manager-latest.deb -Ss
https://mms.mongodb.com/download/agent/automation/mongodb-mms-automation-
agent-manager_latest_amd64.deb  
  
RUN dpkg -i /tmp/mongodb-mms-automation-agent-manager-latest.deb  
  
RUN mkdir /etc/service/mms-agent  
  
ADD start.sh /etc/service/mms-agent/run  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

