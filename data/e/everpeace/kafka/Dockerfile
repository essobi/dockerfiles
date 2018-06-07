# it is derived from alpine:3.4  
FROM java:openjdk-8-jre-alpine  
  
MAINTAINER Shingo Omura <everpeace@gmail.com>  
  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.10.0.0  
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
LABEL name="kafka" version="$SCALA_VERSION"-"$KAFKA_VERSION"  
  
RUN mkdir -p /opt \  
&& apk add --no-cache wget bash sed \  
&& wget -q -O -
http://apache.mirrors.spacedump.net/kafka/$KAFKA_VERSION/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz
| tar -xzf - -C /opt  
  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
  
EXPOSE 9092  
ENV PATH /opt/kafka/bin:$PATH  
CMD ["/usr/bin/start-kafka.sh"]  

