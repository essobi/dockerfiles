FROM alpine  
  
MAINTAINER Igor Grytsyk "gritsyk@gmail.com"  
ENV JAVA_OPTS "-Xms3G -Xmx6G"  
ENV ZK_URL "localhost:2181"  
ENV BROKER_ID 0  
ENV NUM_PARTITIONS 1  
ENV BROKER_PORT 9092  
ENV ADV_HOST "172.31.0.21"  
ENV LOG_RETENTION_HOURS 168  
ENV LOG_SEGMENT_BYTES 1073741824  
ENV LOG_RETENTION_CHECK_INTERVAL_MS 300000  
ENV GROUP_INITIAL_REBALANCE_DELAY_MS 0  
RUN apk add --no-cache \  
bash \  
bash-completion \  
openjdk8-jre-base && \  
mkdir /topic-data  
  
VOLUME /topic-data  
  
COPY kafka /kafka  
  
EXPOSE $BROKER_PORT  
  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]

