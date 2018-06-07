FROM eatcode/openjdk8  
  
MAINTAINER Ayub Malik <ayub.malik@gmail.com>  
  
WORKDIR /opt  
  
ENV KAFKA_VERSION 0.10.0.0  
RUN wget -q -O -
http://mirrors.ukfast.co.uk/sites/ftp.apache.org/kafka/${KAFKA_VERSION}/kafka_2.11-${KAFKA_VERSION}.tgz
| tar -xzf - -C /opt \  
&& ln -s /opt/kafka_2.11-$KAFKA_VERSION /opt/kafka  
  
ENV KAFKA_HOME /opt/kafka  
  
WORKDIR /opt/kafka  
  
LABEL name=buildnum value=5  
  
ADD server.properties config/server.properties  
  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
  
ADD wait-for-it.sh /usr/bin/wait-for-it.sh  
  
ADD wait-for-zookeeper.sh /usr/bin/wait-for-zookeeper.sh  
  
EXPOSE 9092  
CMD ["start-kafka.sh"]  
  

