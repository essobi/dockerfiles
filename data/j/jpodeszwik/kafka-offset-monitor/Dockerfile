FROM dockerfile/java:oracle-java8  
  
RUN \  
echo "deb http://dl.bintray.com/sbt/debian /" >>
/etc/apt/sources.list.d/sbt.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get --yes --force-yes install sbt  
  
RUN \  
git clone -b v0.2.1 https://github.com/quantifind/KafkaOffsetMonitor.git
/KafkaOffsetMonitor && \  
cd /KafkaOffsetMonitor && \  
sbt assembly && \  
mv /KafkaOffsetMonitor/target/scala-*/KafkaOffsetMonitor-assembly-*.jar / && \  
rm -rf /KafkaOffsetMonitor && \  
rm -rf ~/.sbt  
  
ENV REFRESH 120.seconds  
ENV RETAIN 2.days  
  
EXPOSE 8080  
WORKDIR /data  
  
VOLUME ["/data"]  
  
CMD exec java -cp /KafkaOffsetMonitor-assembly-*.jar
com.quantifind.kafka.offsetapp.OffsetGetterWeb --port 8080 --zk $ZK \--refresh
$REFRESH \--retain $RETAIN  

