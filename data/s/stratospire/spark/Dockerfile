FROM java:openjdk-8-jdk  
  
MAINTAINER Ryan C Koch <ryanckoch@gmail.com>  
  
ENV SPARK_VERSION="2.0.0" \  
HADOOP_MAJOR_VERSION="2.7" \  
HADOOP_VERSION="2.7.3"  
# Get Hadoop from US Apache mirror and extract just the native  
# libs. (Until we care about running HDFS with these containers, this  
# is all we need.)  
RUN mkdir -p /opt && \  
cd /opt && \  
curl
http://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
| \  
tar -zx hadoop-${HADOOP_VERSION}/lib/native && \  
ln -s hadoop-${HADOOP_VERSION} hadoop && \  
echo Hadoop ${HADOOP_VERSION} native libraries installed in
/opt/hadoop/lib/native  
# Get Spark from US Apache mirror.  
RUN mkdir -p /opt && \  
cd /opt && \  
curl
http://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop${HADOOP_MAJOR_VERSION}.tgz | \  
tar -zx && \  
ln -s spark-${SPARK_VERSION}-bin-hadoop${HADOOP_MAJOR_VERSION} spark && \  
echo Spark ${SPARK_VERSION} installed in /opt  
  
# Add the GCS connector.  
RUN mkdir /opt/spark/lib && \  
cd /opt/spark/lib && \  
curl -O https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-latest-
hadoop2.jar  
# if numpy is installed on a driver it needs to be installed on all  
# workers, so install it everywhere  
RUN apt-get update && \  
apt-get install -y python-numpy && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD bin/* /  
ADD conf/* /opt/spark/conf/  
ENV PATH $PATH:/opt/spark/bin  

