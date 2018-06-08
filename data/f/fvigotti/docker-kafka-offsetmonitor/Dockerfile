FROM fvigotti/docker-fatjdk8  
  
MAINTAINER fvigotti  
  
RUN \  
wget -q -O /app.jar
https://github.com/quantifind/KafkaOffsetMonitor/releases/download/v0.2.1/KafkaOffsetMonitor-
assembly-0.2.1.jar  
  
EXPOSE 8080  
WORKDIR /data  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["/usr/bin/java"]  
CMD ["-cp", "/app.jar", "com.quantifind.kafka.offsetapp.OffsetGetterWeb", "--
port", "8080"]  

