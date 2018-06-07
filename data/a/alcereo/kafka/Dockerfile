FROM centos:7  
LABEL description="Kafka 1.0.1 - 2.11. \  
To override properties add \"--override $key=$value\" in CMD \  
\- KUCHEEV A.P. \  
"  
  
RUN yum install -y java-1.8.0-openjdk && \  
yum clean all && \  
rm -rf /var/cache/yum  
  
ADD ./add /  
  
RUN curl -O -J -L http://apache-
mirror.rbc.ru/pub/apache/kafka/1.0.1/kafka_2.11-1.0.1.tgz && \  
tar -xf /kafka_2.11-1.0.1.tgz && \  
rm -rf /kafka_2.11-1.0.1.tgz; \  
chmod +x /entrypoint.sh; \  
curl -L https://www.dropbox.com/s/cyd739s43lk5eyn/kafka-influxdb-metrics-
reporter-0.1.0-shaded.jar?dl=0 -o /kafka-influxdb-metrics-
reporter-0.1.0-shaded.jar && \  
mv /kafka-influxdb-metrics-reporter-0.1.0-shaded.jar /kafka_2.11-1.0.1/libs/  
  
ENV KAFKA_DIR="/kafka_2.11-1.0.1"  
ENV BROKER_ID=0  
ENV LISTENERS="PLAINTEXT://:9092"  
ENV ADVERTIZED_LISTENERS="PLAINTEXT://localhost:9092"  
ENV NUM_NETWORK_THREADS=3  
ENV NUM_IO_THREADS=8  
ENV LOG_DIRS="/tmp/kafka-logs"  
ENV ZOOKEEPER_CONNECT="localhost:2181"  
ENV JMX_PORT=8993  
# Metrics  
ENV KAFKA_INFLUXDB_METRICS_REPORTER_ENABLED=false  
ENV KAFKA_INFLUXDB_METRICS_ADDRESS=http://localhost:8086  
ENV KAFKA_INFLUXDB_METRICS_DATABASE=kafka  
ENV KAFKA_INFLUXDB_METRICS_USERNAME=root  
ENV KAFKA_INFLUXDB_METRICS_PASSWORD=root  
  
  
ENTRYPOINT ["/entrypoint.sh"]

