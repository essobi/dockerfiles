FROM dockerfile/java:oracle-java7  
MAINTAINER Harald Westphal <h.westphal@gmx.de>  
  
RUN \  
wget -q -O /app.jar
https://github.com/quantifind/KafkaOffsetMonitor/releases/download/v0.2.0/KafkaOffsetMonitor-
assembly-0.2.0.jar  
  
EXPOSE 8080  
WORKDIR /data  
  
VOLUME ["/data"]  
  
CMD exec java -cp /app.jar com.quantifind.kafka.offsetapp.OffsetGetterWeb
--port 8080 `cat /data/*.conf 2>/dev/null || true`  

