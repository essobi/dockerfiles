FROM ubuntu:16.04  
MAINTAINER Ralf Geschke <ralf@kuerbis.org>  
  
ENV MONGO_USER=mongodb \  
MONGO_DATA_DIR=/var/lib/mongodb \  
MONGO_LOG_DIR=/var/log/mongodb  
  
RUN apt-get update && apt-get -y upgrade \  
&& apt-get install -y --no-install-recommends \  
ca-certificates curl \  
numactl logrotate supervisor \  
&& mkdir -p /var/log/supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp/ && curl -OL
https://cloud.mongodb.com/download/agent/backup/mongodb-mms-backup-
agent_latest_amd64.deb \  
&& dpkg -i mongodb-mms-backup-agent_latest_amd64.deb \  
&& curl -OL https://cloud.mongodb.com/download/agent/monitoring/mongodb-mms-
monitoring-agent_latest_amd64.deb \  
&& dpkg -i mongodb-mms-monitoring-agent_latest_amd64.deb  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["app:start"]  

