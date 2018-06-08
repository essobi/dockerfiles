# Stage 0  
FROM openjdk:8-jdk-alpine AS base_alpine_jdk8  
  
# build jar  
RUN apk add --no-cache git  
RUN git clone https://github.com/SapInnovation/reactiveretail-stock.git  
RUN cd reactiveretail-stock && ./gradlew :stock-stream-processor:assemble
--no-daemon  
  
# Stage 1  
FROM openjdk:8-jdk-alpine  
ENV PROCESSOR_FILE stock-stream-processor-latest.jar  
ENV PROCESSOR_HOME /reactiveretail-stock/stock-stream-processor/build/libs  
  
# Copy jar from previous stage  
COPY \--from=base_alpine_jdk8 $PROCESSOR_HOME/$PROCESSOR_FILE $PROCESSOR_FILE  
  
EXPOSE 8080  
ENTRYPOINT ["sh", "-c"]  
CMD ["exec java -jar $PROCESSOR_FILE \--spring.data.mongodb.uri=$DB_HOST
\--spring.cloud.stream.kafka.binder.brokers=$KAFKA_HOST"]  

