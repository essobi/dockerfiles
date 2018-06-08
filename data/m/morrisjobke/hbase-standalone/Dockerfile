FROM ubuntu:14.04  
MAINTAINER tobe tobeg3oogle@gmail.com  
  
RUN apt-get -y update  
  
# Install Oracle Java7  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get install -y oracle-java7-installer  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/  
  
# Install tools  
RUN apt-get install -y git && \  
apt-get install -y maven  
  
# Install HBase  
RUN git clone git://git.apache.org/hbase.git /hbase  
WORKDIR /hbase  
RUN git checkout 0.98.6 # use specified version  
RUN mvn clean package -DskipTests  
  
# ZooKeeper  
EXPOSE 2181  
# HMaster  
EXPOSE 60000  
# HMaster Web  
EXPOSE 60010  
# RegionServer  
EXPOSE 60020  
# RegionServer Web  
EXPOSE 60030  
# set log level  
RUN sed -i 's/^\\(log4j\\.logger\\.org\\.apache\\.zookeeper=\\)INFO/\1WARN/'
/hbase/conf/log4j.properties && \  
sed -i 's/^\\(log4j\\.logger\\.org\\.apache\\.hadoop\\.hbase=\\)DEBUG/\1WARN/'
/hbase/conf/log4j.properties && \  
sed -i
's/^\\(log4j\\.logger\\.org\\.apache\\.hadoop\\.hbase\\.zookeeper\\.ZKUtil=\\)INFO/\1WARN/'
/hbase/conf/log4j.properties && \  
sed -i
's/^\\(log4j\\.logger\\.org\\.apache\\.hadoop\\.hbase\\.zookeeper\\.ZooKeeperWatcher=\\)INFO/\1WARN/'
/hbase/conf/log4j.properties && \  
sed -i 's/^\\(hbase\\.root\\.logger=\\)INFO/\1WARN/'
/hbase/conf/log4j.properties && \  
sed -i 's/^\\(hbase\\.security\\.logger=\\)INFO/\1WARN/'
/hbase/conf/log4j.properties  
  
CMD ["./bin/hbase", "master", "start"]  

