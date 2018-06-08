FROM java:8-alpine  
  
WORKDIR /hm2mqtt  
RUN apk add --no-cache wget \  
&& wget
https://github.com/owagner/hm2mqtt/releases/download/v0.18d/hm2mqtt.jar  
  
EXPOSE 3333  
ENTRYPOINT ["java", "-jar", "hm2mqtt.jar", "hm.bindaddress=0.0.0.0:3333"]  

