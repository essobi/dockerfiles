FROM linarotechnologies/alpine:edge  
  
RUN apk add --no-cache ca-certificates mosquitto  
  
EXPOSE 1883 8883  
COPY start.sh start.sh  
RUN chmod +x start.sh  
ENTRYPOINT ["/start.sh"]  
  
CMD /usr/sbin/mosquitto -c /etc/mosquitto/conf.d/mosquitto.conf  

