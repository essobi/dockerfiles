FROM ubuntu:16.04  
MAINTAINER helgeho@invelop.de  
  
ENV SPARK_VERSION=2.0.1 \  
HADOOP_VERSION=2.7 \  
ZEPPELIN_VERSION=0.6.2  
ENV TERM xterm  
EXPOSE 8080  
VOLUME /deps /data /notes  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
curl \  
openjdk-8-jdk \  
vim \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Scala and SBT  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823 \  
&& apt-get update && apt-get install -y scala sbt \  
&& rm -rf /var/lib/apt/lists/*  
  
# Spark  
RUN wget http://www-
us.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-
hadoop$HADOOP_VERSION.tgz \  
&& tar xfz spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz \  
&& rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz  
  
# Zeppelin  
RUN wget http://www-
us.apache.org/dist/zeppelin/zeppelin-$ZEPPELIN_VERSION/zeppelin-$ZEPPELIN_VERSION-
bin-netinst.tgz \  
&& tar xfz zeppelin-$ZEPPELIN_VERSION-bin-netinst.tgz \  
&& rm zeppelin-$ZEPPELIN_VERSION-bin-netinst.tgz  
  
# ArchiveSpark  
RUN git clone https://github.com/helgeho/ArchiveSpark.git && cd ArchiveSpark \  
&& sbt assemblyPackageDependency && sbt assembly  
  
WORKDIR zeppelin-$ZEPPELIN_VERSION-bin-netinst  
  
COPY zeppelin-env.sh conf/zeppelin-env.sh.temp  
RUN tr "\r" " " < conf/zeppelin-env.sh.temp > conf/zeppelin-env.sh  
  
CMD bin/zeppelin-daemon.sh start && bash  

