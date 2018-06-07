###### Docker Images  
FROM qnib/hadoop  
  
ENV SCALA_VER=2.10.4 \  
SAMZA_BASE_VER=2.10 \  
SLF4J_VER=1.0.1 \  
SAMZA_VER=0.8.0 \  
HDFS_LIB_DIR=/opt/hadoop/share/hadoop/hdfs/lib \  
HDFS_URL=http://search.maven.org/remotecontent  
  
RUN yum install -y bsdtar maven  
RUN mkdir -p ${HADOOP_YARN_HOME}/share/hadoop/hdfs/lib && \  
curl -fsL http://www.scala-lang.org/files/archive/scala-${SCALA_VER}.tgz |tar
xzf - -C /opt/ && \  
cp /opt/scala-${SCALA_VER}/lib/{scala-compiler.jar,scala-library.jar}
/opt/hadoop/share/hadoop/hdfs/lib/ && \  
rm -rf /opt/scala-${SCALA_VER}  
RUN curl -sLo ${HDFS_LIB_DIR}/grizzled-
slf4j_${SAMZA_BASE_VER}-${SLF4J_VER}.jar
${HDFS_URL}?filepath=org/clapper/grizzled-
slf4j_${SAMZA_BASE_VER}/${SLF4J_VER}/grizzled-
slf4j_${SAMZA_BASE_VER}-${SLF4J_VER}.jar && \  
curl -sLo ${HDFS_LIB_DIR}/samza-yarn_${SAMZA_BASE_VER}-${SAMZA_VER}.jar
${HDFS_URL}?filepath=org/apache/samza/samza-
yarn_${SAMZA_BASE_VER}/${SAMZA_VER}/samza-
yarn_${SAMZA_BASE_VER}-${SAMZA_VER}.jar && \  
curl -sLo ${HDFS_LIB_DIR}/samza-core_${SAMZA_BASE_VER}-${SAMZA_VER}.jar
${HDFS_URL}?filepath=org/apache/samza/samza-
core_${SAMZA_BASE_VER}/${SAMZA_VER}/samza-
core_${SAMZA_BASE_VER}-${SAMZA_VER}.jar  
ADD opt/hadoop/etc/hadoop/core-site.xml /opt/hadoop/etc/hadoop/  
  
## Samza  
RUN yum install -y git-core  
RUN git clone http://git-wip-us.apache.org/repos/asf/samza.git /opt/samza && \  
cd /opt/samza && \  
./gradlew publishToMavenLocal  
  
## Hello Samza  
RUN chown hadoop: /opt/  
USER hadoop  
RUN curl -sfL https://github.com/apache/samza-hello-samza/archive/master.zip
|bsdtar xf - -C /opt/  
RUN cd /opt/samza-hello-samza-master && \  
sed -i -e 's/localhost:2181/zookeeper.service.consul:2181/' build.gradle && \  
mvn clean package  
RUN mkdir -p /opt/samza-hello-samza-master/deploy/ && \  
tar xzf /opt/samza-hello-samza-master/target/hello-samza-0.10.0-dist.tar.gz -C
/opt/samza-hello-samza-master/deploy/ && \  
sed -i -e 's/localhost:2181/zookeeper.service.consul:2181/' /opt/samza-hello-
samza-master/deploy/config/wikipedia-feed.properties && \  
sed -i -e 's/localhost:9092/kafka.service.consul:9092/' /opt/samza-hello-
samza-master/deploy/config/wikipedia-feed.properties && \  
sed -i -e 's/localhost:2181/zookeeper.service.consul:2181/' /opt/samza-hello-
samza-master/deploy/config/wikipedia-parser.properties && \  
sed -i -e 's/localhost:9092/kafka.service.consul:9092/' /opt/samza-hello-
samza-master/deploy/config/wikipedia-parser.properties  
USER root  
ADD opt/qnib/hadoop/bin/yarn.sh /opt/qnib/hadoop/bin/  
RUN chmod 700 /var/empty/sshd && \  
echo "su - hadoop" >> /root/.bash_history && \  
echo "./deploy/bin/run-job.sh --config-
factory=org.apache.samza.config.factories.PropertiesConfigFactory --config-
path=file://$PWD/deploy/config/wikipedia-feed.properties" >>
/home/hadoop/.bash_history && \  
echo "cd /opt/samza-hello-samza-master/" >> /home/hadoop/.bash_history  
  

