FROM alpine:latest  
  
LABEL maintainer="npastorale@gmail.com"  
RUN apk update && \  
apk upgrade && \  
apk --no-cache add mosquitto && \  
mkdir -p /mosquitto/config /mosquitto/data /mosquitto/log && \  
cp /etc/mosquitto/mosquitto.conf /mosquitto/config && \  
chown -R mosquitto:mosquitto /mosquitto  
  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]  

