FROM alpine:3.7  
LABEL Maintainer="Tim de Pater <code@trafex.nl>" \  
Description="Lightweight Mosquitto MQTT server based on Alpine Linux."  
  
# Install packages  
RUN apk --no-cache add mosquitto mosquitto-clients  
  
# Expose MQTT port  
EXPOSE 1883  
ENV PATH /usr/sbin:$PATH  
  
ENTRYPOINT ["/usr/sbin/mosquitto"]  

