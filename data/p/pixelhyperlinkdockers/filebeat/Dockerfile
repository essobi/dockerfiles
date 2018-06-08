# PixelHyperlink Filebeat Docker  
#  
# VERSION 1.3.0  
FROM pixelhyperlinkdockers/ubuntu:v1.8.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with filebeat service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.3.0"  
LABEL com.pixelhyperlink.docker.filebeat.version="1.3.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.filebeat.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.filebeat.version.is-production="true"  
  
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \  
apt-key add - && \  
apt-get -y install apt-transport-https && \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | \  
tee -a /etc/apt/sources.list.d/elastic-5.x.list && \  
apt-get update && \  
apt-get install filebeat  
  
RUN mkdir /var/lib/filebeat /var/log/filebeat  
  
VOLUME ["/var/lib/filebeat", "/var/log/filebeat"]  
  
# Copy filebeat config.  
COPY ./filebeat.yml /etc/filebeat/filebeat.yml  
  
COPY ./filebeat_entrypoint.sh /opt/filebeat_entrypoint.sh  
  
# Run startup scripts  
RUN chmod 777 /opt/filebeat_entrypoint.sh  
  
ENTRYPOINT ["/opt/filebeat_entrypoint.sh"]  

