FROM gudaoxuri/spark:latest AS spark_env  
MAINTAINER gudaoxuri <i@sunisle.org>  
  
FROM gudaoxuri/hive:latest  
  
FROM gudaoxuri/hbase:latest  
  
USER root  
  
# Setup env  
ENV KYLIN_HOME /opt/kylin  
ENV PATH $KYLIN_HOME/bin:$PATH  
ENV KEEP false  
  
RUN echo "export KYLIN_HOME=/opt/kylin" >> /etc/profile  
RUN echo "export PATH=$KYLIN_HOME/bin:$PATH" >> /etc/profile  
  
# Download spark  
RUN wget -q -O - http://mirrors.hust.edu.cn/apache/kylin/apache-
kylin-2.2.0/apache-kylin-2.2.0-bin-hbase1x.tar.gz | tar -xzf - -C /opt/ \  
&& mv /opt/apache-kylin-2.2.0-bin /opt/kylin  
  
COPY kylin.properties $KYLIN_HOME/conf/  
COPY bootstrap_kylin.sh /bin/bootstrap_kylin.sh  
COPY bootstrap.sh /bin/bootstrap.sh  
  
# config kylin use spark  
RUN mkdir $KYLIN_HOME/hadoop-conf  
  
RUN ln -s $HADOOP_HOME/etc/hadoop/core-site.xml $KYLIN_HOME/hadoop-conf/core-
site.xml  
RUN ln -s $HADOOP_HOME/etc/hadoop/hdfs-site.xml $KYLIN_HOME/hadoop-conf/hdfs-
site.xml  
RUN ln -s $HADOOP_HOME/etc/hadoop/yarn-site.xml $KYLIN_HOME/hadoop-conf/yarn-
site.xml  
  
RUN ln -s $HBASE_HOME/conf/hbase-site.xml $KYLIN_HOME/hadoop-conf/hbase-
site.xml  
RUN cp $HIVE_HOME/conf/hive-site.xml $KYLIN_HOME/hadoop-conf/hive-site.xml  
# RUN vi $KYLIN_HOME/hadoop-conf/hive-site.xml (change "hive.execution.engine"
value from "tez" to "mr")  
RUN cp -r $SPARK_HOME/* $KYLIN_HOME/spark  
  
RUN jar cv0f spark-libs.jar -C $KYLIN_HOME/spark/jars/ .  
RUN hadoop fs -mkdir -p /kylin/spark/  
RUN hadoop fs -put spark-libs.jar /kylin/spark/  
  
RUN chmod +x /bin/bootstrap*  
  
EXPOSE 7070  
ENTRYPOINT /bin/bootstrap.sh $KEEP  

