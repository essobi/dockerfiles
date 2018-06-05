FROM dockerfile/java:oracle-java8  
  
RUN wget -qO - http://packages.confluent.io/deb/1.0/archive.key | sudo apt-key
add - && \  
add-apt-repository "deb [arch=all] http://packages.confluent.io/deb/1.0 stable
main" && \  
apt-get update && \  
apt-get install -y confluent-kafka-rest  
  
EXPOSE 8082  
ADD kafka-rest.properties /usr/etc/kafka-rest/kafka-rest.properties  
  
ADD kafka-avro-serializer-1.0.jar /usr/share/java/kafka-rest/kafka-avro-
serializer-1.0.jar  
  
CMD ["/usr/bin/kafka-rest-start", "/usr/etc/kafka-rest/kafka-rest.properties"]  

