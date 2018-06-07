FROM alpine:3.4  
  
RUN apk add \--no-cache mosquitto && \  
rm -Rf /etc/mosquitto/  
  
ADD ./entrypoint.sh /entrypoint.sh  
  
USER mosquitto  
EXPOSE 1883  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]  

