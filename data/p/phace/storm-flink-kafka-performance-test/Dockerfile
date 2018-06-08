#  
# VERSION 0.0.1  
#  
FROM ubuntu  
  
MAINTAINER Attila Balogh-Biró "attila.balogh86@gmail.com"  
# Installing basic stuf: maven, git, jdk  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y git  
RUN apt-get install -y maven  
RUN apt-get install -y wget  
RUN apt-get install -y zookeeperd  
  
# Set environment variables  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ENV KAFKA_VERSION 0.8.2.2  
ENV KAFKA_SCALA_VERSION 2.10  
ENV JMX_PORT 7203  
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
# Register automatic start for zookeeper  
RUN /etc/init.d/zookeeper start  
  
# Create folder for kafka installation  
RUN mkdir -p /kafka /data /logs  
  
ADD
http://www.us.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}
/tmp/  
  
# Install kafka  
RUN tar -xvzf /tmp/${KAFKA_RELEASE_ARCHIVE} \--strip 1 -C /kafka  
  
# Set up a user to run Kafka  
RUN groupadd kafka && \  
useradd -d /kafka -g kafka -s /bin/false kafka && \  
chown -R kafka:kafka /kafka /data /logs  
  
USER kafka  
  
ENV PATH /kafka/bin:$PATH  
  
WORKDIR /kafka  
  
EXPOSE 9092 ${JMX_PORT} VOLUME [ "/data", "/logs" ]  
  
CMD ["nohup /kafka/bin/kafka-server-start.sh /kafka/config/server.properties >
/kafka/kafka.log 2>&1 &"]  
  
# Create topic  
RUN /kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --create
--replication-factor 1 --partition 1 --topic neverwinter  
  
# Pull project from GitHub  
RUN git clone https://github.com/PhaceBP/storm-flink-kafka-performance-
test.git  
  
# Pull forked Nvent project from GitHub  
RUN git clone https://github.com/PhaceBP/interviewQuestions.git  
  
# Step into the project root dir  
WORKDIR "/storm-flink-kafka-performance-test"  
  
# Clean and build the project  
RUN mvn clean install  
  
# Finished  

