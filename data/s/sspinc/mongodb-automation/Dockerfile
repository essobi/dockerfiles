FROM ubuntu:14.04  
MAINTAINER Secret Sauce Partners, Inc. <operations@sspinc.io>  
  
ENV AGENT_PACKAGE mongodb-mms-automation-agent-manager_latest_amd64.deb  
ENV AGENT_PACKAGE_URL
https://cloud.mongodb.com/download/agent/automation/$AGENT_PACKAGE  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates curl \  
libsasl2-2 \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download & install Automation Agent  
RUN set -x \  
&& curl -o /tmp/$AGENT_PACKAGE -SL $AGENT_PACKAGE_URL \  
&& dpkg -i /tmp/$AGENT_PACKAGE \  
&& rm -f /tmp/$AGENT_PACKAGE  
  
# MongoDB data volume  
VOLUME /data  
RUN chown mongodb:mongodb /data  
  
# default MMS automation port  
EXPOSE 27000  
ENTRYPOINT ["/opt/mongodb-mms-automation/bin/mongodb-mms-automation-agent"]  

