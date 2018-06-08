FROM netflixoss/java:8  
ENV KAFKA_MONITOR_PORT=4080  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ca-certificates  
  
RUN apt-get install -y cron  
  
RUN mkdir /kafka-monitor  
  
ADD
https://github.com/quantifind/KafkaOffsetMonitor/releases/download/v0.2.1/KafkaOffsetMonitor-
assembly-0.2.1.jar /kafka-monitor/  
  
WORKDIR /kafka-monitor  
  
ADD start.sh /start.sh  
  
EXPOSE ${KAFKA_MONITOR_PORT}  
  
# CMD ["/start.sh"]  
CMD ["crond", "-f"]  

