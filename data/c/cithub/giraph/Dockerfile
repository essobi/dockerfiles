FROM cithub/hadoop  
MAINTAINER Channel IT Services, LLC  
  
ENV GIRAPH_VER=1.2.0-hadoop2  
ENV GIRAPH_HOME=/home/hadoop/giraph  
ENV HADOOP_VER=2.5.1  
ENV HADOOP_HOME=/home/hadoop/hadoop  
ENV ZOOKEEPER_VER=3.4.10  
ENV ZOOKEEPER_HOME=/home/hadoop/zookeeper  
  
RUN\  
apt-get install -y git maven &&\  
apt-get update &&\  
apt-get clean  
RUN\  
wget http://mirrors.advancedhosters.com/apache/giraph/giraph-1.2.0/giraph-
dist-$GIRAPH_VER-bin.tar.gz &&\  
tar xzvf giraph-dist-$GIRAPH_VER-bin.tar.gz &&\  
mv giraph-1.2.0-hadoop2-for-hadoop-2.5.1 $GIRAPH_HOME &&\  
rm giraph-dist-$GIRAPH_VER-bin.tar.gz &&\  
cd $GIRAPH_HOME &&\  
git clone https://github.com/apache/giraph.git &&\  
cd giraph &&\  
mvn -Phadoop_2 -DskipTests package  
RUN\  
wget
http://mirrors.koehn.com/apache/zookeeper/stable/zookeeper-$ZOOKEEPER_VER.tar.gz
&&\  
tar xzvf zookeeper-$ZOOKEEPER_VER.tar.gz &&\  
mv zookeeper-$ZOOKEEPER_VER $ZOOKEEPER_HOME &&\  
rm zookeeper-$ZOOKEEPER_VER.tar.gz  
RUN\  
mkdir /data/giraph &&\  
mkdir /data/zookeeper  
  
EXPOSE 50030  
VOLUME /data

