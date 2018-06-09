FROM java:8  
MAINTAINER xiao_xing <xingxiao@htsc.com>  
RUN apt-get update  
RUN apt-get install -y wget supervisor  
RUN wget http://mirrors.hust.edu.cn/apache/kafka/1.0.0/kafka_2.11-1.0.0.tgz &&
tar -xzf kafka_2.11-1.0.0.tgz && rm -f kafka_2.11-1.0.0.tgz  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
RUN sed -i "31clisteners=PLAINTEXT://:9092"
/kafka_2.11-1.0.0/config/server.properties \  
&& sed -i "123czookeeper.connect=zookeeper:2181"
/kafka_2.11-1.0.0/config/server.properties \  
&& sed -i "36aadvertised.listeners=PLAINTEXT://kafka:9092"
/kafka_2.11-1.0.0/config/server.properties \  
&& sed -i "36aadvertised.host.name=kafka"
/kafka_2.11-1.0.0/config/server.properties \  
&& sed -i "36ahost.name=kafka" /kafka_2.11-1.0.0/config/server.properties  
ADD create_topics.sh /create_topics.sh  
RUN chmod +x /create_topics.sh  
WORKDIR /kafka_2.11-1.0.0  
EXPOSE 9092  
CMD ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisor/supervisord.conf"]  

