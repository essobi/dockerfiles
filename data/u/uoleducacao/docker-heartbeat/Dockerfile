FROM alpine  
  
WORKDIR /opt/heartbeat  
  
RUN apk --no-cache add --update openssl && \  
wget
https://artifacts.elastic.co/downloads/beats/heartbeat/heartbeat-5.3.0-linux-x86_64.tar.gz
&& \  
tar zxvf *.tar.gz --strip 1 && \  
rm *.tar.gz  
  
CMD ["./heartbeat", "-e", "-c", "heartbeat.yml"]

