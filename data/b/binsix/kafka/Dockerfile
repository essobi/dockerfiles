FROM binsix/openjdk:latest  
MAINTAINER binsix  
LABEL name="kafka" license="MIT" build-date="20180417"  
  
ENV VERSION 1.0.0  
ENV KAFKA_HOME /data/env/kafka  
ENV KAFKA_URL http://www-
us.apache.org/dist/kafka/$VERSION/kafka_2.11-$VERSION.tgz  
ENV PATH $PATH:$KAFKA_HOME/bin:  
  
RUN yum update -y && cd /data/softs && wget "$KAFKA_URL" && tar -zvxf
kafka_2.11-$VERSION.tgz && mv /data/softs/kafka_2.11-$VERSION /data/env/kafka
&& rm -rf /data/softs/*  
  
EXPOSE 9092  
CMD ["kafka-server-start.sh", "/data/env/kafka/config/server.properties"]

