FROM alpine:3.5  
RUN apk --no-cache add curl tar  
  
WORKDIR /filebeat  
RUN curl -sfS
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.2.2-linux-x86_64.tar.gz
\  
| tar -xz --strip-components=1 \  
&& mkdir -p /etc/filebeat \  
&& cp ./filebeat.yml /etc/filebeat/  
  
CMD ["./filebeat", "-e", "-c=/etc/filebeat/filebeat.yml"]  

