FROM youngce/oracle-java:1.8.0_51  
  
####install spark 1.5.1####  
ENV SPARK_VERSION=1.5.1  
ENV HADOOP_VERSION=2.6  
RUN yum install -y tar  
RUN wget
http://ftp.twaren.net/Unix/Web/apache/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-hadoop$HADOOP_VERSION.tgz&& tar -xvzf spark-$SPARK_VERSION-bin-
hadoop$HADOOP_VERSION.tgz  
ENV SPARK_HOME=/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION  
ENV PATH=$PATH:$SPARK_HOME/bin  

