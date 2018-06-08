FROM debian:jessie  
MAINTAINER Allan Lei <allan.lei@orbweb.com>  
  
ENV VERSION 0.12.5p2  
  
RUN apt-get update && \  
apt-get install -y curl ca-certificates sudo libssl1.0.0 sudo logrotate && \  
curl -v -k -L
https://bintray.com/artifact/download/erlio/vernemq/deb/jessie/vernemq_0.12.5p2-1_amd64.deb
> /tmp/vernemq.deb && \  
dpkg -i /tmp/vernemq.deb && \  
apt-get remove -y curl  
# 1883/tcp: MQTT  
# 8883/tcp: MQTT Over SSL  
# 8888/tcp: MQTT over Websocket  
# 8889/tcp: MQTT over Websocket over SSL  
EXPOSE 1883/tcp 8883/tcp 8888/tcp 8889/tcp  
CMD vernemq start && tail -F /var/log/vernemq/console.log  

