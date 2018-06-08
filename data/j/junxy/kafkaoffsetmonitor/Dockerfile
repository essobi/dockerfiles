FROM openjdk:8u131-jre-alpine  
  
MAINTAINER ayijun@gmail.com  
  
RUN mkdir -p /kafkaoffsetmonitor/data  
  
RUN apk add --update curl \  
&& rm -rf /var/cache/apk/*  
RUN curl -s -L \  
-o /kafkaoffsetmonitor/KafkaOffsetMonitor.jar \  
https://github.com/Morningstar/kafka-offset-
monitor/releases/download/0.4.1/KafkaOffsetMonitor-assembly-0.4.1-SNAPSHOT.jar  
  
# RUN apk add --update ca-certificates wget \  
# && update-ca-certificates \  
# && rm -rf /var/cache/apk/*  
# RUN wget -q -O /kafkaoffsetmonitor/KafkaOffsetMonitor.jar \  
# https://github.com/Morningstar/kafka-offset-
monitor/releases/download/0.4.1/KafkaOffsetMonitor-assembly-0.4.1-SNAPSHOT.jar  
ADD start.sh /kafkaoffsetmonitor/start.sh  
  
WORKDIR /kafkaoffsetmonitor  
VOLUME /kafkaoffsetmonitor/data  
EXPOSE 8080  
CMD ["/kafkaoffsetmonitor/start.sh"]  

