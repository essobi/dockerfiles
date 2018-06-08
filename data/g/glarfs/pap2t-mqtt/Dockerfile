FROM alpine  
ENV PAP2T_MQTT_HOST 192.168.1.1 \  
PAP2T_MQTT_PORT 1883 \  
PAP2T_MQTT_ENTRYPOINT /test/phone \  
PAP2T_HOST 192.168.1.10 \  
PAP2T_POOLING 10  
RUN mkdir /app && chown nobody /app  
RUN apk add --no-cache curl mosquitto-clients bash gawk sed grep bc coreutils  
WORKDIR /app  
VOLUME ["/app"]  
USER nobody  
ADD *.sh /app/  
ENTRYPOINT ["/bin/bash"]  
CMD ["/app/daemon-calls.sh" ]  

