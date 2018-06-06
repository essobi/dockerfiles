FROM cgswong/confluent-rest-proxy:1.0.1  
ADD ft-kafka_proxy/templates/log4j.properties.erb /etc/kafka-
rest/log4j.properties  
ENV KAFKAREST_HEAP_OPTS=-Xmx1g  
  
CMD [ "/usr/local/bin/kafka-rest-docker.sh" ]  

