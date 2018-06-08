FROM pulsepointinc/centos7-java8:latest  
  
ENV \  
KOM_CHECKOUT=c9993a5aeb701c08bf679f3ca9e27e5678b62629 \  
KOMG_CHECKOUT=b5a96c64cabb855cf0723e0cb2dde41fa677fbf0  
  
RUN curl -o /etc/yum.repos.d/bintray-sbt-rpm.repo \  
https://bintray.com/sbt/rpm/rpm && \  
yum install -y sbt git && \  
git clone https://github.com/quantifind/KafkaOffsetMonitor.git
/tmp/kafkaoffsetmonitor && \  
cd /tmp/kafkaoffsetmonitor && \  
git checkout ${KOM_CHECKOUT} && \  
sbt publishM2 && \  
mkdir /cp && \  
cp target/scala-*/*.jar /cp && \  
git clone https://github.com/allegro/kafka-offset-monitor-graphite.git
/tmp/kafkaoffsetmonitorgraphite && \  
cd /tmp/kafkaoffsetmonitorgraphite && \  
git checkout ${KOMG_CHECKOUT} && \  
sbt "set test in Test := {}" assembly && \  
cp target/scala-*/*.jar /cp && \  
yum autoremove -y git sbt && \  
yum clean all && \  
rm -rf /root/.m2 /root/.sbt /root/.ivy2 /tmp/*  
  
EXPOSE 8080  
  
COPY start.sh /start.sh  
  
CMD ["/start.sh"]  

