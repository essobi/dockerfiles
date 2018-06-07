FROM kingcontext/confluent-platform:confluent2  
  
ENV ENDPOINT_TYPE producer  
  
ENV KAFKA_HOST kafka  
ENV KAFKA_PORT 9092  
ENV TOPIC test  
ENV INTERVAL 1  
ENV ZOOKEEPER_HOST zookeeper  
ENV ZOOKEEPER_PORT 2181  
ENV SCHEMA_REGISTRY_HOST schema-registry  
ENV SCHEMA_REGISTRY_PORT 8081  
ENV MESSAGE_SCHEMA
'{"type":"record","name":"myrecord","fields":[{"name":"f1","type":"string"}]}'  
ENV MESSAGE_PAYLOAD '{"f1": "value1"}'  
RUN apt-get install -y telnet netcat tcpdump  
  
ADD kafka-producer.sh /kafka-producer.sh  
RUN chmod 755 /kafka-producer.sh  
  
ADD kafka-consumer.sh /kafka-consumer.sh  
RUN chmod 755 /kafka-consumer.sh  
  
ADD kafka-endpoint.sh /kafka-endpoint.sh  
RUN chmod 755 /kafka-endpoint.sh  
  
ENTRYPOINT ["/kafka-endpoint.sh"]  

