# PixelHyperlink Ubuntu with Heartbeat Docker  
#  
# VERSION 1.0.0  
FROM pixelhyperlinkdockers/ubuntu:v1.8.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with heartbeat service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.0.0"  
LABEL com.pixelhyperlink.docker.heartbeat.version="1.0.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.heartbeat.release-date="2017-07-08"  
LABEL com.pixelhyperlink.docker.heartbeat.version.is-production="true"  
  
RUN mkdir /var/log/heartbeat /var/lib/heartbeat  
  
VOLUME ["/var/log/heartbeat"]  
  
# Copy heartbeat setup.  
COPY ./heartbeat /opt/heartbeat  
  
# Install heartbeat  
RUN dpkg -i /opt/heartbeat/heartbeat-5.5.0-amd64.deb  
  
# Copy heartbeat config.  
COPY ./heartbeat.yml /etc/heartbeat/heartbeat.yml  
  
COPY ./heartbeat_entrypoint.sh /opt/heartbeat_entrypoint.sh  
  
# Run startup scripts  
RUN chmod 777 /opt/heartbeat_entrypoint.sh  
  
ENTRYPOINT ["/opt/heartbeat_entrypoint.sh"]  

