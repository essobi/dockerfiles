FROM java:7-jre  
  
RUN wget -q -O -
http://mirror.vorboss.net/apache/kafka/0.8.1.1/kafka_2.9.2-0.8.1.1.tgz | tar
-xzf - -C / \  
&& mv /kafka_2.9.2-0.8.1.1 /kafka  
  
VOLUME ["/data"]  
  
EXPOSE 9092  
ADD server.properties.initial /server.properties  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
  
CMD start-kafka.sh  
  

