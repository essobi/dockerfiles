FROM ubuntu:16.04  
RUN echo '2017-01-19' && \  
apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qq install openjdk-8-jre-headless wget
supervisor dnsutils && \  
rm -rf /var/lib/apt/lists/* /var/cache/*  
  
ARG SCALA_VERSION=2.11  
ARG KAFKA_VERSION=1.1.0  
ENV KAFKA_HOME=/home/kafka/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
RUN adduser --disabled-password --gecos '' kafka  
USER kafka  
WORKDIR /home/kafka  
  
RUN wget -q
http://www.mirrorservice.org/sites/ftp.apache.org/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O kafka.tgz && \  
tar xfz kafka.tgz && \  
ln -s "kafka_${SCALA_VERSION}-${KAFKA_VERSION}" "kafka" && \  
rm kafka.tgz && \  
mkdir /tmp/kafka-logs  
  
ENV PATH="$PATH:/home/kafka/kafka_${SCALA_VERSION}-${KAFKA_VERSION}/bin"  
ADD start-kafka.sh supervisord.conf ./  
  
# 2181 is zookeeper, 9092 is kafka  
EXPOSE 2181 9092  
VOLUME /tmp/kafka-logs  
  
CMD ["supervisord"]  

