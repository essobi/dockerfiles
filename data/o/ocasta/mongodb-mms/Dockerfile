FROM centos:centos7  
MAINTAINER Martin Higham <martin@ocasta.com>  
  
RUN yum install logrotate -y && yum clean all  
  
RUN curl -sSL https://mms.mongodb.com/download/agent/monitoring/mongodb-mms-
monitoring-agent-latest.x86_64.rhel7.rpm -o mms.rpm \  
&& rpm -U mms.rpm \  
&& rm mms.rpm  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
USER mongodb-mms-agent  
CMD ["mongodb-mms-monitoring-agent", "-conf", "/etc/mongodb-mms/monitoring-
agent.config"]  

