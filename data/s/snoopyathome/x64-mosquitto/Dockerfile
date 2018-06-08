FROM alpine:3.7  
RUN apk add --update ca-certificates mosquitto &&\  
adduser -h /home/service -D -s /bin/false service &&\  
rm -rf /var/cache/apk/*  
  
USER service  
  
CMD ["mosquitto", "-c", "/configuration/mosquitto.conf"]  

