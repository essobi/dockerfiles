# Blatently copied from https://github.com/primait/docker-filebeat  
FROM debian:jessie  
  
ENV FILEBEAT_VERSION=5.1.1  
RUN set -x && \  
apt-get update && \  
apt-get install -y wget supervisor && \  
wget
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz
-O /opt/filebeat.tar.gz && \  
cd /opt && \  
tar xzvf filebeat.tar.gz && \  
cd filebeat-* && \  
cp filebeat /bin && \  
cd /opt && \  
rm -rf filebeat* && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Docker Gen  
WORKDIR /opt  
  
RUN wget https://github.com/jwilder/docker-gen/releases/download/0.7.3/docker-
gen-linux-amd64-0.7.3.tar.gz  
RUN tar xvzf docker-gen-linux-amd64-0.7.3.tar.gz  
  
COPY filebeat.conf /etc/supervisor/conf.d/  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

