FROM debian:wheezy  
MAINTAINER Kousha Najafi <kousha@lazyhack.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends curl
openjdk-7-jre-headless  
  
RUN mkdir -p /opt/kom  
  
ENV KOM_VERSION 0.2.1  
RUN curl --silent -L -o /opt/kom/KafkaOffsetMonitor.jar
https://github.com/quantifind/KafkaOffsetMonitor/releases/download/v$KOM_VERSION/KafkaOffsetMonitor-
assembly-$KOM_VERSION.jar  
  
ENV ZOOKEEPERS zookeeper:2181  
ENV KOM_REFRESH 1.minutes  
ENV KOM_RETENTION 2.days  
ENV PORT 80  
EXPOSE $PORT  
  
CMD java -cp /opt/kom/KafkaOffsetMonitor.jar
com.quantifind.kafka.offsetapp.OffsetGetterWeb --zk "${ZOOKEEPERS}" \--refresh
"${KOM_REFRESH}" \--retain "${KOM_RETENTION}" \--port "${PORT}"  

