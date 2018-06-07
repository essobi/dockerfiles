FROM java:openjdk-8-jre  
  
MAINTAINER Jeremy Babcock <>  
  
RUN [ "mkdir", "/commafeed", "/config", "/data" ]  
COPY ./config.example.yml /config/config.yml  
  
ENV COMMAFEED_VERSION 2.2.0  
ADD
https://github.com/Athou/commafeed/releases/download/$COMMAFEED_VERSION/commafeed.jar
/commafeed/  
  
VOLUME [ "/config", "/data" ]  
  
ENV JAVA_OPTS -Xmx128m  
  
WORKDIR /data  
ENTRYPOINT java ${JAVA_OPTS} -Djava.security.egd=file:/dev/urandom
-Djava.net.preferIPv4Stack=true -jar /commafeed/commafeed.jar server
/config/config.yml  

