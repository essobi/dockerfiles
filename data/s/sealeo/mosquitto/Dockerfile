FROM alpine:3.6  
  
LABEL maintainer="Pierre GUINAULT <speed@sealeo.org>"  
  
LABEL Description="Eclipse Mosquitto MQTT Broker"  
RUN apk --no-cache add mosquitto mosquitto-clients && \  
mkdir -p /mosquitto/config /mosquitto/data /mosquitto/log && \  
chown -R mosquitto:mosquitto /mosquitto  
  
ADD config /mosquitto/config  
  
VOLUME ["/mosquitto/config", "/mosquitto/data", "/mosquitto/log"]  
  
EXPOSE 1883 9001  
  
ADD docker-entrypoint.sh /usr/bin/  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]  
CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]  

