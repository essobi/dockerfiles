FROM ubuntu:14.04  
MAINTAINER prameswar <engg.pram1@gmail.com>  
  
ENV VERSION=1.1.2  
RUN apt-get update && \  
apt-get install -y wget  
  
RUN wget
https://download.elastic.co/beats/filebeat/filebeat_${VERSION}_amd64.deb && \  
dpkg -i filebeat_${VERSION}_amd64.deb && \  
rm filebeat_${VERSION}_amd64.deb  
  
COPY filebeat.yml /etc/filebeat/filebeat.yml  
COPY filebeat.template.json /etc/filebeat/filebeat.template.json  
  
COPY start.sh /start.sh  
  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  
  

