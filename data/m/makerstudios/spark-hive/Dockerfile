FROM openjdk:8u92-jdk-alpine  
  
RUN apk add -U curl bash python3 openssl  
RUN ln -s /usr/bin/python3 /usr/bin/python  
RUN easy_install-3.5 boto3  
  
# If we try to build Spark with its bundled Hadoop 2.7, we get  
# an error: `No FileSystem for scheme: s3n`. So we install Hadoop  
# separately.  
# cf. https://github.com/gettyimages/docker-
spark/blob/707a2ac8aa44ee36f74dc651d06dda3bcab37911/Dockerfile  
ENV HADOOP_VERSION=2.7.3  
ENV HADOOP_HOME /usr/hadoop-$HADOOP_VERSION  
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop  
ENV PATH $PATH:$HADOOP_HOME/bin  
RUN curl -sL \  
"https://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz"
\  
| gunzip \  
| tar -x -C /usr/ \  
&& rm -rf $HADOOP_HOME/share/doc \  
&& chown -R root:root $HADOOP_HOME  
  
ENV SPARK_VERSION=2.0.1  
ENV SPARK_HOME /spark-"$SPARK_VERSION"  
ENV
SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"  
ENV PATH $PATH:$SPARK_HOME/bin  
ADD build-spark.sh /usr/bin/  
RUN /usr/bin/build-spark.sh "$SPARK_VERSION"  
  
WORKDIR $SPARK_HOME  
CMD ["spark-shell"]  

