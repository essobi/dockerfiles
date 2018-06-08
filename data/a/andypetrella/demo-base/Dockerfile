FROM debian:jessie  
  
EXPOSE 80 9160 9042 9200 7077 38080 38081 6060 6061 8090 8099 10000 50070
50090 9092 6066 9000 19999 6379 6081 7474 8787 5601 8989 7979 4040 4041 4042
4043 4044 4045  
# Data Fellas  
MAINTAINER Data Fellas info@data-fellas.guru  
  
USER root  
  
ENV HOME /root  
  
ARG BRANCH_TAG=master  
ARG SPARK_VERSION=1.6.1  
ARG HADOOP_VERSION=2.2.0  
ARG SCALA_VERSION=2.10.5  
ARG GUAVA_VERSION=16.0.1  
RUN echo "deb http://repos.mesosphere.io/debian jessie main" | tee
/etc/apt/sources.list.d/mesosphere.list  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get -qq update --fix-missing \  
&& apt-get -qq -y install apt-utils \  
&& apt-get -qq -y install wget \  
&& apt-get -qq -y install curl \  
&& apt-get -qq -y install git \  
&& apt-get -qq -y install unzip \  
&& apt-get -qq -y install vim \  
&& apt-get -qq -y install screen \  
&& apt-get -qq -y install openssh-server \  
&& apt-get -qq -y install --no-install-recommends openjdk-7-jdk
mesos=0.26.0-0.2.145.debian81  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
ENV MESOS_JAVA_NATIVE_LIBRARY /usr/local/lib/libmesos-0.26.0.so  
  
ENV MESOS_LOG_DIR /var/log/mesos  
  
# Feth base repo  
RUN \  
cd /root \  
&& git clone https://github.com/data-fellas/demo-base.git \  
&& cd demo-base \  
&& chmod a+rx *.sh  
  
# Apache Cassandra  
RUN \  
cd /root \  
&& wget -q https://s3.eu-central-1.amazonaws.com/spark-
notebook/traning/apache-cassandra-2.2.0-bin.tar.gz \  
&& tar xzf apache-cassandra-2.2.0-bin.tar.gz \  
&& rm apache-cassandra-2.2.0-bin.tar.gz  
  
# Apache Kafka (Confluent Distribution)  
RUN \  
cd /root \  
&& wget -q https://s3.eu-central-1.amazonaws.com/spark-
notebook/traning/confluent-1.0-2.10.4.tar.gz \  
&& tar xzf confluent-1.0-2.10.4.tar.gz \  
&& rm confluent-1.0-2.10.4.tar.gz  
  
# SBT  
ADD https://dl.bintray.com/sbt/native-packages/sbt/0.13.8/sbt-0.13.8.tgz
/root/  
  
RUN \  
cd /root/ \  
&& tar xzf sbt-0.13.8.tgz \  
&& rm sbt-0.13.8.tgz  
  
# Spark Notebook  
Run \  
cd /root \  
&& git clone https://github.com/andypetrella/spark-notebook.git git-spark-
notebook \  
&& cd git-spark-notebook \  
&& git checkout $BRANCH_TAG \  
&& /root/sbt/bin/sbt --error 'set showSuccess := false'
-Dspark.version=$SPARK_VERSION -Dscala.version=$SCALA_VERSION
-Dhadoop.version=$HADOOP_VERSION -Dguava.version=$GUAVA_VERSION
-Dwith.hive=true -Dwith.parquet=true "universal:packageZipTarball" \  
&& cp target/universal/spark-notebook*gz .. \  
&& cd .. \  
&& tar xzf spark-notebook*gz \  
&& rm *gz \  
&& mv spark-notebook-* spark-notebook  
  
# Have a directory to mount data directory on host  
RUN \  
cd /root \  
mkdir data  
  
WORKDIR /root/demo-base  

