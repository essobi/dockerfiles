# Build:  
# docker build -t learnshiva/kafta:latest .  
#  
# Create:  
# docker create -it -p 6379:6379 --name container-kafta learnshiva/kafta  
#  
# Start:  
# docker start container-kafta  
#  
# Connect with kafta client  
# docker exec -it container-kafta kafta-cli  
#  
# Connect bash  
# docker exec -it container-kafta bash  
FROM ubuntu:latest  
MAINTAINER Siva <learn.shiva@gmail.com>  
  
ENV SCALA_VERSION 2.10  
ENV KAFKA_VERSION 0.9.0.1  
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
RUN apt-get update && \  
apt-get install -y wget supervisor dnsutils curl  
RUN apt-get install -y zookeeper  
RUN apt-get install -y openjdk-7-jdk openjdk-7-jre && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
wget -q
http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \  
tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \  
rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz  
  
ADD scripts/start-kafka.sh /usr/bin/start-kafka.sh  
  
# Supervisor config  
ADD supervisor/kafka.conf supervisor/zookeeper.conf /etc/supervisor/conf.d/  
  
# 2181 is zookeeper, 9092 is kafka  
EXPOSE 2181 9092  
CMD ["supervisord", "-n"]  

