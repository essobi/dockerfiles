FROM lucitec/base-java8  
  
MAINTAINER Lucitec  
RUN apt-get install -y unzip git  
  
RUN wget -q
http://mirror.gopotato.co.uk/apache/kafka/0.8.1.1/kafka_2.10-0.8.1.1.tgz -O
/tmp/kafka_2.10-0.8.1.1.tgz  
RUN tar xfz /tmp/kafka_2.10-0.8.1.1.tgz -C /opt  
  
ENV KAFKA_HOME /opt/kafka_2.10-0.8.1.1  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
CMD start-kafka.sh  

