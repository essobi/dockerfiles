FROM wurstmeister/kafka:0.10.0.0  
MAINTAINER CloudTrackInc1  
  
RUN java -version  
  
ADD . /tmp/build  
RUN cd /tmp/build && \  
./gradlew -Dorg.gradle.native=false build && \  
cp build/libs/kubernetes-expander-1.0-SNAPSHOT.jar $KAFKA_HOME/libs/  
  
ADD kafka-autoextend-partitions.sh /usr/bin/kafka-autoextend-partitions.sh  
  
CMD echo "Hello, World" | $KAFKA_HOME/bin/kafka-console-producer.sh --broker-
list 192.168.27.185:9092 --topic demo-topic_y

