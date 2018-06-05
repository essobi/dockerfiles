FROM poad/docker-hadoop-amazon:2.8  
MAINTAINER Kenji Saito  
  
#support for Hadoop 2.8.x  
ENV SPARK_HOME /usr/local/spark  
  
RUN SPARK_VERSION=2.2.1 && \  
curl -s
https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-without-hadoop.tgz | tar -xz -C /usr/local/ && \  
cd /usr/local && ln -s spark-$SPARK_VERSION-bin-without-hadoop spark  
RUN mkdir $SPARK_HOME/yarn-remote-client  
ADD yarn-remote-client $SPARK_HOME/yarn-remote-client  
  
RUN SPARK_VERSION=2.2.1 && \  
$BOOTSTRAP && $HADOOP_PREFIX/bin/hadoop dfsadmin -safemode leave &&
$HADOOP_PREFIX/bin/hdfs dfs -put $SPARK_HOME-$SPARK_VERSION-bin-without-
hadoop/jars /spark  
  
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop  
ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin  
  
#install R  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm && \  
yum -y install R  
  
# update boot script  
COPY bootstrap.sh /etc/bootstrap.sh  
RUN chown root.root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
COPY spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf  
  
RUN rm -rf /var/cache/yum/* && \  
yum clean all  
  
ENTRYPOINT ["/etc/bootstrap.sh"]  

