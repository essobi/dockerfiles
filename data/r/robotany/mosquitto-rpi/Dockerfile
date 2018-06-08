FROM resin/raspberrypi3-alpine:3.6  
MAINTAINER David Audet <david.audet@ca.com>  
  
RUN [ "cross-build-start" ]  
  
LABEL Description="Eclipse Mosquitto MQTT Broker"  
RUN apk --no-cache add mosquitto=1.4.12-r0 && \  
mkdir -p /mosquitto/config /mosquitto/data /mosquitto/log && \  
cp /etc/mosquitto/mosquitto.conf /mosquitto/config && \  
chown -R mosquitto:mosquitto /mosquitto  
  
COPY docker-entrypoint.sh /  
RUN chmod 775 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]  
  
RUN [ "cross-build-end" ]  

