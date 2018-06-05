FROM openjdk:8-jre-alpine  
WORKDIR /app  
ENV KAFKA_PORT 9092  
ENV KAFKA_ADVERTISED_HOST 127.0.0.1  
ENV PATH="/app/utils:${PATH}"  
COPY utils/ /app/utils/  
COPY supervisord.conf /app/supervisord.conf  
COPY configureKafka.sh /app/configureKafka.sh  
RUN chmod a+x /app/configureKafka.sh && \  
chmod a+x /app/utils/* && \  
mkdir logs && \  
apk update && apk add bash && apk add libc6-compat && apk add supervisor && \  
wget "https://archive.apache.org/dist/kafka/0.8.2.2/kafka_2.10-0.8.2.2.tgz" &&
\  
tar xvzf kafka_2.10-0.8.2.2.tgz && rm kafka_2.10-0.8.2.2.tgz  
CMD /usr/bin/supervisord -c /app/supervisord.conf

