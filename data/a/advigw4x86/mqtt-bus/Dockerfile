FROM alpine  
MAINTAINER @advantech  
RUN (apk add --no-cache mosquitto mosquitto-clients && rm -rf
/var/cache/apk/*)  
EXPOSE 1883  
ENTRYPOINT ["/usr/sbin/mosquitto"]  

