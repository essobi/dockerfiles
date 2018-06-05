FROM ubuntu:16.04  
MAINTAINER Alexander De Leon "alex@devialab.com"  
ENV REFRESHED_AT 2018-05-10  
RUN apt-get -qqy update && \  
apt-get install -qqy \  
ca-certificates \  
libsasl2-2  
  
# MMS automation  
VOLUME /var/lib/mongodb-mms-automation  
ADD https://cloud.mongodb.com/download/agent/automation/mongodb-mms-
automation-agent-manager_latest_amd64.deb /root/mongodb-mms-automation-agent-
manager_latest_amd64.deb  
RUN dpkg -i /root/mongodb-mms-automation-agent-manager_latest_amd64.deb  
  
# MongoDB data volume  
VOLUME /data  
RUN chown mongodb:mongodb /data  
  
# default MMS automation port  
EXPOSE 27000  
ENTRYPOINT ["/opt/mongodb-mms-automation/bin/mongodb-mms-automation-agent"]  

