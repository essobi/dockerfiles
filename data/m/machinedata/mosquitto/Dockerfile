FROM alpine:3.5  
  
# add user and group first so their IDs don't change  
RUN addgroup mosquitto && adduser -G mosquitto -D -H mosquitto  
  
# su/sudo with proper signaling inside docker  
RUN apk add \--no-cache su-exec  
  
ENV MOSQUITTO_VERSION="1.4.10-r2"  
RUN set -xe \  
&& apk add \--no-cache --virtual .mosquitto \  
mosquitto=${MOSQUITTO_VERSION} \  
mosquitto-libs=${MOSQUITTO_VERSION} \  
mosquitto-clients=${MOSQUITTO_VERSION} \  
\  
&& mkdir /config /data \  
&& cp /etc/mosquitto/mosquitto.conf /config/mosquitto.conf.dist \  
&& chown -R mosquitto:mosquitto /data /config  
  
VOLUME ["/config", "/data"]  
EXPOSE 1883 8883 9001  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["mosquitto", "-c", "/config/mosquitto.conf"]  

