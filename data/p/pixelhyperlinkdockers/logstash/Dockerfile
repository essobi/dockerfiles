# PixelHyperlink Logstash Docker  
#  
# VERSION 1.2.0  
FROM pixelhyperlinkdockers/javajdk:v1.1.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with Java JDK and
logstash service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.2.0"  
LABEL com.pixelhyperlink.docker.logstash.version="1.2.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.logstash.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.logstash.version.is-production="true"  
  
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \  
apt-key add - && \  
apt-get -y install apt-transport-https && \  
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | \  
tee -a /etc/apt/sources.list.d/elastic-5.x.list && \  
apt-get update && \  
apt-get -y install logstash  
  
EXPOSE 5044 9600-9700  
VOLUME ["/var/lib/logstash", "/var/log/logstash"]  
  
# Copy logstash config.  
COPY ./logstash.yml /etc/logstash/logstash.yml  
COPY ./logstash_filter.conf /etc/logstash/conf.d/logstash_filter.conf  
  
COPY ./logstash_entrypoint.sh /opt/logstash_entrypoint.sh  
  
# Run startup scripts  
RUN chmod 777 /opt/logstash_entrypoint.sh  
  
ENTRYPOINT ["/opt/logstash_entrypoint.sh"]  

