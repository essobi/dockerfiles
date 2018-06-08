# Fetch Kafka  
FROM alpine AS fetch  
  
ARG SCALA_VERSION="2.11"  
ARG KAFKA_VERSION="1.1.0"  
ARG
KAFKA_SHA512="5e613dbb21c2aed797e18bb5638386267c4f61ee00d10760dbc6bd472af8b6aa9cdca30c1f93f5e31a3ad8c506374a7350357e2ac2b9a3ddf87caf22820d470e"  
COPY mirrors.txt /tmp/mirrors.txt  
RUN apk add --no-cache curl ca-certificates tar  
  
WORKDIR /tmp  
RUN curl -v --fail -Lo /tmp/kafka.tgz -g "$(shuf -n1
/tmp/mirrors.txt)/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"  
RUN echo "${KAFKA_SHA512} kafka.tgz" | sha512sum -c  
RUN mkdir -p /opt/kafka  
RUN tar --strip-components=1 -xzf /tmp/kafka.tgz -C /opt/kafka  
RUN rm /opt/kafka/config/server.properties  
  
# Build runtime environment  
FROM java:openjdk-8-jre  
  
ENV KAFKA_HOME /opt/kafka  
EXPOSE 9092  
VOLUME ["/data"]  
  
COPY \--from=fetch /opt/kafka /opt/kafka  
COPY scripts /usr/local/bin  
  
ENTRYPOINT ["/usr/local/bin/start-kafka.sh"]  

