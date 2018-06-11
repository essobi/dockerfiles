FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y curl logrotate  
  
# Get latest from https://mms.mongodb.com/  
RUN curl -sSL https://mms.mongodb.com/download/agent/automation/mongodb-mms-
automation-agent-manager_2.0.6.1148-1_amd64.deb -o mms.deb  
RUN dpkg -i mms.deb  
RUN rm mms.deb  
  
ADD entrypoint.sh /usr/bin/entrypoint.sh  
RUN chmod +x /usr/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  
USER mongodb  
CMD ["/opt/mongodb-mms-automation/bin/mongodb-mms-automation-
agent","-f","/etc/mongodb-mms/automation-agent.config"]  

