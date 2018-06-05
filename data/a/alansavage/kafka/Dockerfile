FROM zookeeper  
ENV
KAFKA_ADVERTISED_LISTENERS_HOSTNAME=${KAFKA_ADVERTISED_LISTENERS_HOSTNAME:-127.0.0.1}  
ENV KAFKA_LOG_RETENTION_HOURS=${KAFKA_LOG_RETENTION_HOURS:--1}  
EXPOSE 2181  
EXPOSE 9092  
WORKDIR /  
RUN ["mv", "docker-entrypoint.sh", "configure-zookeeper.sh"]  
COPY docker-entrypoint.sh .  
RUN ["wget", "http://apache.mirror.anlx.net/kafka/1.0.0/kafka_2.11-1.0.0.tgz"]  
ENTRYPOINT ["bash", "docker-entrypoint.sh"]  

