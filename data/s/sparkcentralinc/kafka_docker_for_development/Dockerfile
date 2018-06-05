FROM openjdk:8-jre-alpine  
WORKDIR /app  
ENV KAFKA_HOST localhost  
ENV KAFKA_PORT 9092  
ENV KAFKA_INTERNAL_HOST kafka  
ENV KAFKA_INTERNAL_PORT 9093  
ENV
KAFKA_LISTENERS="INTERNAL://:${KAFKA_INTERNAL_PORT},PLAINTEXT://:${KAFKA_PORT}"  
ENV
KAFKA_ADVERTISED_LISTENERS="INTERNAL://${KAFKA_INTERNAL_HOST}:${KAFKA_INTERNAL_PORT},PLAINTEXT://${KAFKA_HOST}:${KAFKA_PORT}"  
ENV PATH="/app/utils:${PATH}"  
COPY utils/ /app/utils/  
COPY supervisord.conf /app/supervisord.conf  
COPY configureKafka.sh /app/configureKafka.sh  
RUN chmod a+x /app/configureKafka.sh && \  
chmod a+x /app/utils/* && \  
mkdir logs && \  
apk update && apk add bash && apk add libc6-compat && apk add supervisor && \  
wget "https://archive.apache.org/dist/kafka/1.0.1/kafka_2.11-1.0.1.tgz" && \  
tar xvzf kafka_2.11-1.0.1.tgz && rm kafka_2.11-1.0.1.tgz  
CMD /usr/bin/supervisord -c /app/supervisord.conf

