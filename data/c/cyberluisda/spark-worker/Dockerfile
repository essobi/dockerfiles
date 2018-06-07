FROM mesosphere/mesos:1.1.0-2.0.107.ubuntu1404  
  
# Install Oracle JDK instead of OpenJDK  
RUN apt-get remove -y --auto-remove openjdk* && \  
apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-
selections && \  
sudo apt-get install -y oracle-java8-installer oracle-java8-set-default && \  
rm -r /var/cache/oracle-jdk*  
  
# Update the base ubuntu image with dependencies needed for Spark  
RUN apt-get install -y python libnss3 curl unzip  
  
ENV SPARK_VERSION 2.1.0  
ENV HADOOP_VERSION 2.7  
  
RUN mkdir /usr/lib/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} && \  
curl
http://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION}.tgz \  
| tar --strip-components=1 -xzC /usr/lib/spark-${SPARK_VERSION}-bin-
hadoop${HADOOP_VERSION} && \  
rm -fr /usr/lib/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/examples  
#Add hadoop s3 support  
RUN curl
"https://search.maven.org/remotecontent?filepath=org/apache/hadoop/hadoop-
aws/2.7.3/hadoop-aws-2.7.3.jar" \  
-o /usr/lib/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/jars/hadoop-aws-2.7.3.jar && \  
curl "https://search.maven.org/remotecontent?filepath=com/amazonaws/aws-java-
sdk/1.7.4/aws-java-sdk-1.7.4.jar" \  
-o /usr/lib/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/jars/aws-java-sdk-1.7.4.jar  
  
ENV SPARK_HOME /usr/lib/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}  
ENV PATH $PATH:/usr/lib/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/bin  
ENV MESOS_NATIVE_JAVA_LIBRARY /usr/local/lib/libmesos.so  

