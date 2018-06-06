FROM java:openjdk-8-jre  
  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.9.0.1  
RUN curl
http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
| tar xvz --strip-components=1  
  
WORKDIR /bin  

