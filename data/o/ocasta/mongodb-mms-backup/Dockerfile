FROM centos:centos7  
MAINTAINER Martin Higham <martin@ocasta.com>  
  
RUN yum install logrotate -y && yum clean all  
  
RUN curl -sSL https://mms.mongodb.com/download/agent/backup/mongodb-mms-
backup-agent-latest.x86_64.rhel7.rpm -o mms.rpm \  
&& rpm -U mms.rpm \  
&& rm mms.rpm  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
USER mongodb-mms-agent  
CMD ["mongodb-mms-backup-agent", "-c", "/etc/mongodb-mms/backup-agent.config"]  

