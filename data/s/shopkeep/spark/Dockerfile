FROM java:openjdk-8  
ENV HADOOP_HOME /opt/spark/hadoop-2.6.0  
ENV MESOS_VERSION 0.26.0  
ENV MESOS_NATIVE_LIBRARY /opt/libmesos-$MESOS_VERSION.so  
ENV SBT_VERSION 0.13.8  
ENV SCALA_VERSION 2.11.7  
RUN mkdir /opt/spark  
WORKDIR /opt/spark  
  
# Install Scala  
RUN \  
cd /root && \  
curl -o scala-$SCALA_VERSION.tgz
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz &&
\  
tar -xf scala-$SCALA_VERSION.tgz && \  
rm scala-$SCALA_VERSION.tgz && \  
echo >> /root/.bashrc && \  
echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc  
  
# Update sbt package  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb  
  
# Install  
RUN \  
apt-get update && \  
apt-get install -y build-essential sbt python-dev python-boto libcurl4-nss-dev
libsasl2-dev libsasl2-2 libsasl2-modules maven libapr1-dev libsvn-dev
zlib1g-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN update-alternatives --set java /usr/lib/jvm/java-8-openjdk-
amd64/jre/bin/java  
  
RUN \  
curl http://d3kbcqa49mib13.cloudfront.net/spark-1.4.0-bin-hadoop2.6.tgz | tar
-zx --strip-components=1 && \  
curl
http://www.apache.org/dist/mesos/$MESOS_VERSION/mesos-$MESOS_VERSION.tar.gz |
tar -zx && cd mesos-$MESOS_VERSION && ./configure && make && \  
curl
http://supergsego.com/apache/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz |
tar -zx && \  
mv /opt/spark/mesos-$MESOS_VERSION/src/.libs/libmesos-$MESOS_VERSION.so /opt
&& \  
rm -rf /opt/spark/mesos-$MESOS_VERSION  

