FROM debian:wheezy  
MAINTAINER mateuszmoneta@gmail.com  
  
ENV MMS_VERSION=5.7.0.368\  
MMS_USER=mms  
  
RUN apt-get update \  
&& apt-get install -qqy --force-yes --no-install-recommends logrotate
libsasl2-2 ca-certificates wget\  
&& wget https://cloud.mongodb.com/download/agent/monitoring/mongodb-mms-
monitoring-agent_$MMS_VERSION-1_amd64.deb -O mms.deb\  
&& dpkg -i mms.deb\  
&& rm mms.deb\  
&& useradd $MMS_USER\  
&& chown $MMS_USER /etc/mongodb-mms/monitoring-agent.config\  
&& apt-get purge -y wget\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /entrypoint.sh  
USER $MMS_USER  
  
ENTRYPOINT /entrypoint.sh  

