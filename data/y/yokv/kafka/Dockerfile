FROM java:8-jre-alpine  
MAINTAINER yokv ez4tzl@hotmail.com  
  
ENV SCALA_VERSION 2.12  
ENV KAFKA_VERSION 1.1.0  
RUN wget -c
http://archive.apache.org/dist/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O - | tar -xz -C /  
RUN apk add --no-cache bash  
WORKDIR /kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
  
EXPOSE 9092  
CMD ["/bin/sh", "-c", "bin/kafka-server-start.sh config/server.properties"]  

