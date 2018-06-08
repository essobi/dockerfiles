# PixelHyperlink Ubuntu with Packetbeat Docker  
#  
# VERSION 1.0.0  
FROM pixelhyperlinkdockers/ubuntu:v1.8.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with packetbeat
service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.0.0"  
LABEL com.pixelhyperlink.docker.packetbeat.version="1.0.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.packetbeat.release-date="2017-07-08"  
LABEL com.pixelhyperlink.docker.packetbeat.version.is-production="true"  
  
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \  
apt-key add - && \  
apt-get -y install apt-transport-https && \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | \  
tee -a /etc/apt/sources.list.d/elastic-5.x.list && \  
apt-get update && \  
apt-get install -y packetbeat  
  
RUN mkdir /var/log/packetbeat /var/lib/packetbeat  
  
VOLUME ["/var/log/packetbeat", "/var/lib/packetbeat"]  
  
# Copy packetbeat config.  
COPY ./packetbeat.yml /etc/packetbeat/packetbeat.yml  
  
COPY ./packetbeat_entrypoint.sh /opt/packetbeat_entrypoint.sh  
  
# Run startup scripts  
RUN chmod 777 /opt/packetbeat_entrypoint.sh  
  
ENTRYPOINT ["/opt/packetbeat_entrypoint.sh"]  

