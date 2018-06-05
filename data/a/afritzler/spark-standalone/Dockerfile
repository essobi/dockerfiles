FROM ubuntu:14.04  
MAINTAINER Andreas Fritzler <andreas.fritzler@gmail.com>  
  
RUN apt-get -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes software-
properties-common python-software-properties  
RUN apt-add-repository -y ppa:webupd8team/java  
RUN apt-get -y update  
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java7-installer
oracle-java7-set-default  
  
RUN apt-get -y install curl  
  
#Download SPARK  
RUN curl -s http://www.eu.apache.org/dist/spark/spark-1.5.1/spark-1.5.1-bin-
hadoop2.6.tgz | tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s spark-1.5.1-bin-hadoop2.6 spark  
  
# Install SPARK JobServer  
ENV SPARK_SERVER_HOME /spark-jobserver/runner  
  
RUN curl -O http://apt.typesafe.com/repo-deb-build-0002.deb && \  
dpkg -i repo-deb-build-0002.deb && \  
apt-get update && \  
apt-get install -y --no-install-recommends sbt \  
git-core \  
build-essential \  
apt-utils \  
&& \  
rm repo-deb-build-0002.deb  
  
#Install SBT  
RUN mkdir -p /root/.sbt/.lib/0.13.7  
WORKDIR /root/.sbt/.lib/0.13.7  
RUN wget --quiet "https://repo.typesafe.com/typesafe/ivy-releases/org.scala-
sbt/sbt-launch/0.13.7/sbt-launch.jar"  
  
#build jobserver repo  
RUN git clone https://github.com/spark-jobserver/spark-jobserver.git
/tmp/spark-jobserver  
WORKDIR /tmp/spark-jobserver  
## Comment out all tests  
RUN sed -r -i "s/\/\/ test/test/g" project/Assembly.scala  
RUN sbt job-server/assembly  
RUN mkdir -p $SPARK_SERVER_HOME && \  
cp /tmp/spark-jobserver/bin/server_start.sh $SPARK_SERVER_HOME && \  
cp /tmp/spark-jobserver/bin/server_stop.sh $SPARK_SERVER_HOME && \  
cp /tmp/spark-jobserver/job-server/target/scala-2.10/spark-job-server.jar
$SPARK_SERVER_HOME  
  
# upload JobServer config  
ADD config/log4j-server.properties $SPARK_SERVER_HOME/log4j-server.properties  
ADD config/settings.sh $SPARK_SERVER_HOME/settings.sh  
ADD config/settings.conf $SPARK_SERVER_HOME/settings.conf  
  
# upload Spark config  
ADD scripts/start-master.sh /start-master.sh  
ADD scripts/start-worker.sh /start-worker.sh  
ADD scripts/start-jobserver.sh /start-jobserver.sh  
RUN chmod a+rwx /start-jobserver.sh  
ADD scripts/start-all.sh /start-all.sh  
ENV SPARK_HOME /usr/local/spark  
  
ENV SPARK_MASTER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_WORKER_OPTS="-Dspark.driver.port=7001 -Dspark.fileserver.port=7002
-Dspark.broadcast.port=7003 -Dspark.replClassServer.port=7004
-Dspark.blockManager.port=7005 -Dspark.executor.port=7006 -Dspark.ui.port=4040
-Dspark.broadcast.factory=org.apache.spark.broadcast.HttpBroadcastFactory"  
ENV SPARK_MASTER_PORT 7077  
ENV SPARK_MASTER_WEBUI_PORT 8080  
ENV SPARK_WORKER_PORT 8888  
ENV SPARK_WORKER_WEBUI_PORT 8081  
ENV SPARK_WORKER_CORE=5  
# Clean up  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Port of the JobServer  
EXPOSE 8090 8080 4040 8081  
WORKDIR /  
CMD ["./start-all.sh"]  

