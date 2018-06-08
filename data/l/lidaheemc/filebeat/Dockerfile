FROM frolvlad/alpine-glibc  
MAINTAINER lida.he@dell.com  
  
ENV FILEBEAT_VERSION=5.2.0  
RUN apk add --no-cache \  
ca-certificates \  
curl  
  
RUN curl -L -O
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz
&& \  
tar -xvvf filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz && \  
mv filebeat-${FILEBEAT_VERSION}-linux-x86_64/ /filebeat && \  
mv /filebeat/filebeat.yml /filebeat/filebeat.example.yml && \  
chmod +x /filebeat/filebeat && \  
mkdir -p /filebeat/config /filebeat/data  
  
WORKDIR /filebeat  
  
COPY entrypoint.sh /filebeat/entrypoint.sh  
COPY filebeat.yml /filebeat/filebeat.yml  
  
ENTRYPOINT ["/filebeat/entrypoint.sh"]  
CMD ["/filebeat/filebeat", "-e", "-v", "-c", "/filebeat/filebeat-out.yml"]  

