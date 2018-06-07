FROM jongoks/docker-jdk  
  
#Download  
RUN wget -q
http://apache.mirror.cdnetworks.com/kafka/0.11.0.1/kafka_2.11-0.11.0.1.tgz  
  
#Install  
RUN tar -xzf kafka_2.11-0.11.0.1.tgz -C /opt && rm /kafka_2.11-0.11.0.1.tgz  
  
#Config  
RUN sed -i
"s|zookeeper.connect=localhost:2181|zookeeper.connect=ltrees.net:2181|g"
/opt/kafka_2.11-0.11.0.1/config/server.properties  
RUN sed -i "s|#delete.topic.enable=true|delete.topic.enable=true|g"
/opt/kafka_2.11-0.11.0.1/config/server.properties  
RUN sed -i
"s|#advertised.listeners=PLAINTEXT://your.host.name:9092|advertised.listeners=PLAINTEXT://ltrees.net:9092|g"
/opt/kafka_2.11-0.11.0.1/config/server.properties  
  
WORKDIR /opt/kafka_2.11-0.11.0.1  
  
EXPOSE 9092  
CMD ["bin/kafka-server-start.sh", "config/server.properties"]  

