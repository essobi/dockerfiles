FROM ubuntu:16.04  
  
  
MAINTAINER slamhan1987@hotmail.com  
  
  
RUN apt-get update \  
&& apt-get install -y curl unzip  
  
# JAVA  
ARG JAVA_MAJOR_VERSION=8  
ARG JAVA_UPDATE_VERSION=112  
ARG JAVA_BUILD_NUMBER=15  
ENV JAVA_HOME /usr/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}  
  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN curl -sL --retry 3 --insecure \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/server-
jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man  
  
# HADOOP  
ENV HADOOP_VERSION 2.7.3  
ENV HADOOP_HOME /usr/hadoop-$HADOOP_VERSION  
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop  
ENV PATH $PATH:$HADOOP_HOME/bin  
RUN curl -sL --retry 3 \  
"http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz"
\  
| gunzip \  
| tar -x -C /usr/ \  
&& rm -rf $HADOOP_HOME/share/doc \  
&& chown -R root:root $HADOOP_HOME  
# SPARK  
ENV SPARK_VERSION 2.1.0  
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-without-hadoop  
ENV
SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"  
ENV SPARK_HOME /usr/spark  
ENV PATH $PATH:${SPARK_HOME}/bin  
RUN curl -sL —retry 3 \  
"http://d3kbcqa49mib13.cloudfront.net/${SPARK_PACKAGE}.tgz" \  
| gunzip \  
| tar x -C /usr/ \  
&& mv /usr/$SPARK_PACKAGE $SPARK_HOME \  
&& chown -R root:root $SPARK_HOME \  
&& curl -sL "http://central.maven.org/maven2/mysql/mysql-connector-
java/5.1.40/mysql-connector-java-5.1.40.jar" -o /usr/spark/jars/mysql-
connector-java.jar  
  
WORKDIR $SPARK_HOME  
  
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]  

