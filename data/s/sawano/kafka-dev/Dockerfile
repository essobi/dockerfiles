#  
# Builds a Kafka image to play around with. Includes Kafka (with Zookeeper),
kafka-monitor, and kafka manager.  
# Why a docker image? To get rid of the hassle/time of installing and building
the tools included.  
# Care have been taken to make the image size as small as possible.  
#  
# /kafka/start_all.sh will start up a Kafka cluster with 3 brokers  
#  
# Refer to documentation to start playing around:  
# https://kafka.apache.org/quickstart  
# https://github.com/linkedin/kafka-monitor  
# https://github.com/yahoo/kafka-manager  
#  
# Quickstart commands:  
#  
# docker build -t sawano/kafka-dev:0.10.1.0 .  
# docker run -it -p 2181:2181 -p 9092:9092 -p 9093:9093 -p 9094:9094 -p
8000:8000 -p 9000:9000 \--name kafka-dev sawano/kafka-dev:0.10.1.0  
# /kafka/start_all.sh  
# /kafka-monitor/start.sh  
# http://localhost:8000/index.html (kafka-monitor)  
# /kafka-manager/start.sh  
# http://localhost:9000/ (kakfa-manager)  
#  
#  
  
FROM alpine:3.4  
MAINTAINER Daniel Sawano  
ENV HOME /root  
RUN apk add --no-cache \  
vim \  
bash  
  
#######################  
# install Kafka  
#######################  
WORKDIR /kafka  
RUN apk add --no-cache curl tar && \  
curl -O "http://www-eu.apache.org/dist/kafka/0.10.1.0/kafka_2.11-0.10.1.0.tgz"
&& \  
tar --strip-components=1 -xzf kafka_2.11-0.10.1.0.tgz && \  
#curl -LO "https://github.com/apache/kafka/archive/0.10.1.0.tar.gz" && \  
#tar --strip-components=1 -xzf 0.10.1.0.tar.gz && \  
apk del tar curl  
  
RUN mkdir logs  
  
RUN touch start_zookeeper.sh; chmod +x start_zookeeper.sh && \  
echo "pushd /kafka" >> start_zookeeper.sh && \  
echo "nohup bin/zookeeper-server-start.sh config/zookeeper.properties >
logs/zookeeper.out 2>&1 &" >> start_zookeeper.sh && \  
echo "popd" >> start_zookeeper.sh  
  
RUN touch start_kafka_server.sh; chmod +x start_kafka_server.sh && \  
echo "pushd /kafka" >> start_kafka_server.sh && \  
echo "nohup bin/kafka-server-start.sh config/server.properties >
logs/kafka.out 2>&1 &" >> start_kafka_server.sh && \  
echo "popd" >> start_kafka_server.sh  
  
######  
# setup broker config  
######  
  
RUN cp config/server.properties config/server-1.properties && \  
cp config/server.properties config/server-2.properties  
  
RUN sed -i -- 's/broker.id=0/broker.id=1/g' config/server-1.properties && \  
sed -i -- 's|#listeners=PLAINTEXT://:9092|listeners=PLAINTEXT://:9093|g'
config/server-1.properties && \  
sed -i -- 's|log.dirs=/tmp/kafka-logs|log.dirs=/tmp/kafka-logs-1|g'
config/server-1.properties  
  
RUN sed -i -- 's|broker.id=0|broker.id=2|g' config/server-2.properties && \  
sed -i -- 's|#listeners=PLAINTEXT://:9092|listeners=PLAINTEXT://:9094|g'
config/server-2.properties && \  
sed -i -- 's|log.dirs=/tmp/kafka-logs|log.dirs=/tmp/kafka-logs-2|g'
config/server-2.properties  
  
RUN touch start_cluster.sh; chmod +x start_cluster.sh && \  
echo "pushd /kafka" >> start_cluster.sh && \  
echo "nohup bin/kafka-server-start.sh config/server-1.properties > logs/kafka-
node-1.out 2>&1 &" >> start_cluster.sh && \  
echo "nohup bin/kafka-server-start.sh config/server-2.properties > logs/kafka-
node-2.out 2>&1 &" >> start_cluster.sh && \  
echo "popd" >> start_cluster.sh  
  
# start_all.sh  
RUN touch start_all.sh; chmod +x start_all.sh && \  
echo "pushd /kafka" >> start_all.sh && \  
echo "echo Starting Zookeeper..." >> start_all.sh && \  
echo "./start_zookeeper.sh" >> start_all.sh && \  
echo "sleep 3" >> start_all.sh && \  
echo "echo Started zookeeper." >> start_all.sh && \  
echo "echo Starting Kafka server..." >> start_all.sh && \  
echo "./start_kafka_server.sh" >> start_all.sh && \  
echo "echo Started Kafka server." >> start_all.sh && \  
echo "sleep 3" >> start_all.sh && \  
echo "echo Starting Kafka cluster nodes..." >> start_all.sh && \  
echo "./start_cluster.sh" >> start_all.sh && \  
echo "echo Started Kafka cluster nodes." >> start_all.sh && \  
echo "popd" >> start_all.sh  
  
  
#######################  
# install kafka-monitor  
#######################  
WORKDIR /kafka-monitor  
RUN apk add --no-cache openjdk8 libstdc++ git && \  
git clone --depth 1 https://github.com/linkedin/kafka-monitor.git . && \  
./gradlew jar && \  
rm -rf ~/.gradle && \  
apk del openjdk8 libstdc++ git  
  
RUN mkdir logs  
  
RUN touch start.sh; chmod +x start.sh && \  
echo "pushd /kafka-monitor" >> start.sh && \  
echo "nohup bin/kafka-monitor-start.sh config/kafka-monitor.properties >
logs/kafka-monitor.out 2>&1 &" >> start.sh && \  
echo "popd" >> start.sh  
  
#######################  
# install kafka-manager  
#######################  
  
ENV KAFKA_MANAGER_VERSION 1.3.1.8  
WORKDIR /kafka-manager  
RUN apk add --no-cache openjdk8 unzip curl tar && \  
mkdir source; cd source && \  
curl -LO https://github.com/yahoo/kafka-
manager/archive/"$KAFKA_MANAGER_VERSION".tar.gz && \  
tar --strip-components=1 -xzf "$KAFKA_MANAGER_VERSION".tar.gz && \  
# Following line is a workaround for SBTs inability to download sbt-launch.jar  
mkdir -p $HOME/.sbt/launchers/0.13.9; curl -L -o
$HOME/.sbt/launchers/0.13.9/sbt-launch.jar http://dl.bintray.com/typesafe/ivy-
releases/org.scala-sbt/sbt-launch/0.13.9/sbt-launch.jar && \  
./sbt clean dist && \  
cp target/universal/kafka-manager-"$KAFKA_MANAGER_VERSION".zip .. && \  
cd .. && \  
rm -rf source && \  
unzip kafka-manager-"$KAFKA_MANAGER_VERSION".zip && \  
rm kafka-manager-"$KAFKA_MANAGER_VERSION".zip && \  
rm -rf kafka-manager-"$KAFKA_MANAGER_VERSION"/share/doc && \  
rm -rf ~/.ivy2 && \  
rm -rf ~/.sbt && \  
apk del openjdk8 unzip curl tar  
  
RUN mkdir logs  
  
RUN touch start.sh; chmod +x start.sh && \  
echo "pushd /kafka-manager/kafka-manager-$KAFKA_MANAGER_VERSION" >> start.sh
&& \  
echo "bin/kafka-manager > /kafka-manager/logs/kafka-monitor.out 2>&1 &" >>
start.sh  
  
RUN sed -i -- 's/kafka-manager-zookeeper/localhost/g' kafka-
manager-"$KAFKA_MANAGER_VERSION"/conf/application.conf  
  
# We only need JRE for running  
RUN apk add --no-cache openjdk8-jre  
  
EXPOSE 2181 9092 9093 9094 8000 9000  
CMD /bin/bash  

