FROM phenompeople/centos-sunjdk:ML  
LABEL project="apache-spark"  
ARG SPARK_VERSION=2.2.0  
ARG HADOOP_VERSION=2.7  
RUN useradd -u 404 spark  
RUN wget -q -O /tmp/spark.tgz
http://redrockdigimark.com/apachemirror/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz && \  
tar -xzf /tmp/spark.tgz -C /usr/local && \  
ln -sf /usr/local/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}
/usr/local/spark && \  
rm -rf /tmp/spark.tgz  
ENV SPARK_HOME=/usr/local/spark  
ENV PATH=${SPARK_HOME}/bin:$PATH  
ENTRYPOINT ["spark-submit","--version"]  

