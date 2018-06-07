FROM alpine:3.5  
ENV FILEBEAT_VERSION 5.4.0  
RUN apk update && \  
apk add wget && \  
wget
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz
--no-check-certificate && \  
tar xzf filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz && \  
mv filebeat-${FILEBEAT_VERSION}-linux-x86_64/filebeat /usr/local/bin && \  
rm -rf /filebeat* && \  
apk del wget  
  
COPY filebeat.yml /etc/filebeat/  
  
CMD ["/usr/local/bin/filebeat", "-e", "-c", "/etc/filebeat/filebeat.yml"]  

