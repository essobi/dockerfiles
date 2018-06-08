###########################################  
## Spark 1.5.1 over Hadoop 2.6 over Ubuntu  
  
FROM sequenceiq/hadoop-ubuntu:2.6.0  
  
###########################################  
# From http://www.eu.apache.org/dist/spark/spark-1.5.1/  
ENV SPARK_VERSION spark-1.5.1  
ENV HADOOP_VERSION hadoop2.6  
ENV ZOOKEEPER_VERSION zookeeper-3.4.6  
ENV SPARK_BIN "$SPARK_VERSION-bin-$HADOOP_VERSION"  
ENV SPARK_URL
"http://www.eu.apache.org/dist/spark/$SPARK_VERSION/$SPARK_BIN.tgz"  
  
###########################################  
# Spark  
RUN curl $SPARK_URL | tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s $SPARK_BIN spark  
ENV SPARK_HOME /usr/local/spark  
  
###########################################  
ENV SPARK_JAR $SPARK_HOME/lib/$SPARK_BIN.jar  
ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin  
RUN echo "spark.master\tspark://master:7077" \  
> $SPARK_HOME/conf/spark-defaults.conf  
  
###########################################  
# Zookeeper  
ENV ZOOKEEPER_HOME = /home/cluster/zookeeper  
RUN mkdir -p $ZOOKEEPER_HOME  
RUN cd $ZOOKEEPER_HOME  
RUN wget
https://www.apache.org/dist/zookeeper/$ZOOKEEPER_VERSION/$ZOOKEEPER_VERSION.tar.gz  
RUN tar –zxvf zookeeper-3.4.6.tar.gz  
RUN mkdir –p $ZOOKEEPER_HOME/data/  
RUN mkdir –p $ZOOKEEPER_HOME/log/  
  
###########################################  
# This is necessary to make things work in a cluster  
# where slave datanodes will search for  
ENV MYHOSTNAME master  
# Set the right name for configuration  
RUN sed "s/HOSTNAME/$MYHOSTNAME/" \  
$HADOOP_PREFIX/etc/hadoop/core-site.xml.template > \  
$HADOOP_PREFIX/etc/hadoop/core-site.xml  
  
VOLUME ["/data"]  
  
ENV HADOOP_CONF "/Data/Hadoop/conf"  
  
# Bootstraps for master and workers  
ENV BSMASTER /bootmaster.sh  
# sed -i.bak 's/value>1/value>0/'g $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
# yes Y | hdfs namenode -format  
RUN echo "#!/bin/bash" > $BSMASTER && \  
echo "spark-class org.apache.spark.deploy.master.Master &\nsleep 5" \  
>> $BSMASTER && \  
echo "echo 'starting namenode'" >> $BSMASTER && \  
echo "service ssh start && $HADOOP_PREFIX/sbin/start-dfs.sh --config
HADOOP_CONF > /dev/null 2>&1 &\nsleep 5" >> $BSMASTER  
  
# hdfs dfsadmin -safemode leave  
ENV BSWORKER /bootslave.sh  
RUN echo "#!/bin/bash" > $BSWORKER && \  
echo "spark-class org.apache.spark.deploy.worker.Worker spark://master:7077"
>> $BSWORKER  
RUN chmod +x $BSWORKER $BSMASTER  
  
#EXPOSE 7077  
#CMD ["$BSMASTER"]  
  
###########################################  
# WORKER test operation  
# hdfs dfs -put /data/books/pg1232.txt hdfs://master:9000/mybook.txt  

