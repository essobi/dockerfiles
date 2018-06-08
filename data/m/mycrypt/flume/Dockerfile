FROM mycrypt/debian-java  
MAINTAINER Bai Xiaoyong lostitle@gmail.com  
  
RUN mkdir /opt/flume  
RUN wget -qO- https://archive.apache.org/dist/flume/1.5.0/apache-
flume-1.5.0-bin.tar.gz \  
| tar zxvf - -C /opt/flume --strip 1  
  
RUN apt-get install -y sudo git  
  
RUN git clone https://github.com/beyondj2ee/flumeng-kafka-plugin /opt/flumeng-
kafka-plugin  
WORKDIR /opt/flumeng-kafka-plugin  
  
#RUN sed -i -e"s/^producer.sources.s.type\s*=\s*seq/producer.sources.s.type =
exec/" flumeng-kafka-plugin/conf/flume-conf.properties  
#RUN sed -i -e'/type = exec/a producer.sources.s.command = tail -f -n+1
/mydata/test.log' flumeng-kafka-plugin/conf/flume-conf.properties  
RUN sed -i -e"s/^producer.sources.s.type\s*=\s*seq/producer.sources.s.type =
netcat/" flumeng-kafka-plugin/conf/flume-conf.properties  
RUN sed -i -e'/type = netcat/a producer.sources.s.bind =
0.0.0.0\nproducer.sources.s.port = 44444' flumeng-kafka-plugin/conf/flume-
conf.properties  
RUN sed -i
-e"s/^producer.sinks.r.metadata.broker.list\s*=\s*127.0.0.1:9092/producer.sinks.r.metadata.broker.list=kafka:9092/"
flumeng-kafka-plugin/conf/flume-conf.properties  
RUN sed -i
-e"s/^consumer.sources.s.zookeeper.connect\s*=\s*127.0.0.1:2181/consumer.sources.s.zookeeper.connect=zookeeper:2181/"
flumeng-kafka-plugin/conf/flume-conf.properties  
  
RUN sed -i
-e"s/^producer.sinks.r.custom.topic.name\s*=\s*kafkaToptic/producer.sinks.r.custom.topic.name=defenseInDepth/"
flumeng-kafka-plugin/conf/flume-conf.properties  
RUN sed -i
-e"s/^consumer.sources.s.custom.topic.name\s*=\s*kafkaToptic/consumer.sources.s.custom.topic.name=defenseInDepth/"
flumeng-kafka-plugin/conf/flume-conf.properties  
RUN cp flumeng-kafka-plugin/conf/flume-conf.properties /opt/flume/conf  
RUN cp flumeng-kafka-plugin/package/flumeng-kafka-plugin.jar /opt/flume/lib  
RUN cp flumeng-kafka-plugin/libs/*.jar /opt/flume/lib  
  
RUN echo "PATH=/opt/flume/bin:$PATH" >> /etc/environment  
ENV PATH /opt/flume/bin:$PATH  
  
RUN echo "\  
[program:flume]\n\  
command=/opt/flume/bin/flume-ng agent --conf conf --conf-file
/opt/flume/conf/flume-conf.properties --name producer
-Dflume.root.logger=INFO,console\n\  
" >> /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 44444  

