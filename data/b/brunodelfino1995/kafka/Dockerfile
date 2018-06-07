FROM alpine  
  
ENV SCALA_VERSION=2.11 \  
KAFKA_VERSION=0.10.1.0 \  
KAFKA_HOME=/opt/kafka \  
HOME=/home/kafka  
  
WORKDIR $HOME  
# Install Kafka to its home directory  
RUN \  
apk update && \  
apk upgrade && \  
apk add ruby bash openjdk8-jre-base wget tar supervisor && \  
wget -t 20 --retry-connrefused -O
"kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"
"http://mirror.nbtelecom.com.br/apache/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz"
&& \  
tar zxf "kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz" && \  
rm -f "kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz" && \  
mkdir -p /opt && mv "kafka_${SCALA_VERSION}-${KAFKA_VERSION}" $KAFKA_HOME  
# Add configuration files  
ONBUILD ARG CONFIG_FOLDER=config  
ONBUILD COPY $CONFIG_FOLDER config  
  
# Supervisor config  
COPY supervisor /etc/supervisor.d/  
  
# Copy necessary files  
COPY . .  
  
# 2181 = Zookeper  
# 9092 = Kafka  
EXPOSE 2181 9092  
  
CMD bin/start  

