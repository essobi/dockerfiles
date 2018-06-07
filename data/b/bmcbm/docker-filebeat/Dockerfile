FROM ubuntu:xenial  
  
MAINTAINER Casper Bruun <cbm@berlingskemedia.dk>  
  
ENV REFRESHED_AT "2016-08-12 09:15:00"  
ENV FILEBEAT_VERSION=5.0.0-alpha4 \  
FILEBEAT_SHA1=49086e2916a13e80d2913779d5d224bcea929f5e  
  
RUN set -x && \  
apt-get update && \  
apt-get install -y wget && \  
wget
https://download.elastic.co/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz
-O /opt/filebeat.tar.gz && \  
cd /opt && \  
echo "${FILEBEAT_SHA1} filebeat.tar.gz" | sha1sum -c - && \  
tar xzvf filebeat.tar.gz && \  
cd filebeat-* && \  
cp filebeat /bin && \  
cd /opt && \  
rm -rf filebeat* && \  
apt-get purge -y wget && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD [ "filebeat", "-e" ]  

