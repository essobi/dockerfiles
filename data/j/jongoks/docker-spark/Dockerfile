FROM jongoks/docker-python3  
  
MAINTAINER Jongoks <jongoks@gmail.com>  
  
# http://blog.stuart.axelbrooke.com/python-3-on-spark-return-of-the-
pythonhashseed  
ENV PYTHONHASHSEED 0  
ENV PYTHONIOENCODING UTF-8  
ENV PIP_DISABLE_PIP_VERSION_CHECK 1  
  
# jdk  
RUN apt-get update && apt-get install -y openjdk-8-jdk  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
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
ENV SPARK_VERSION 2.2.0  
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-without-hadoop  
ENV SPARK_HOME /usr/spark-${SPARK_VERSION}  
ENV
SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"  
ENV PATH $PATH:${SPARK_HOME}/bin  
RUN curl -sL --retry 3 \  
"http://d3kbcqa49mib13.cloudfront.net/${SPARK_PACKAGE}.tgz" \  
| gunzip \  
| tar x -C /usr/ \  
&& mv /usr/$SPARK_PACKAGE $SPARK_HOME \  
&& chown -R root:root $SPARK_HOME  
  
WORKDIR $SPARK_HOME  
  
EXPOSE 7077 8080  

