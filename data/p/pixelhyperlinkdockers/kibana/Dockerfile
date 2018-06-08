# PixelHyperlink Kibana Docker  
#  
# VERSION 1.1.0  
FROM pixelhyperlinkdockers/ubuntu:v1.8.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with Kibana service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.1.0"  
LABEL com.pixelhyperlink.docker.kibana.version="1.1.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.kibana.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.kibana.version.is-production="true"  
  
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \  
apt-key add - && \  
apt-get -y install apt-transport-https && \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | \  
tee -a /etc/apt/sources.list.d/elastic-5.x.list && \  
apt-get update && \  
apt-get -y install kibana  
  
EXPOSE 5601  
VOLUME ["/var/log/kibana"]  
  
# Copy logstash config.  
COPY ./kibana.yml /etc/kibana/kibana.yml  
  
RUN mkdir /var/run/kibana  
  
COPY ./kibana_entrypoint.sh /opt/kibana_entrypoint.sh  
  
# Run startup scripts  
RUN chmod 777 /opt/kibana_entrypoint.sh  
  
ENTRYPOINT ["/opt/kibana_entrypoint.sh"]  

