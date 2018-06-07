FROM fullstackml/spark-base  
MAINTAINER Dmitry Petrov <dmitry@fullstackml.com>  
  
LABEL com.fullstackml = "true" \  
com.fullstackml.function = "base-docker-images/spark-hadoop-base" \  
com.fullstackml.version = "1.0"  
  
# Install Hadoop  
RUN wget http://www-
eu.apache.org/dist/hadoop/common/hadoop-2.7.2/hadoop-2.7.2.tar.gz 2>/dev/null
&& \  
tar zxf hadoop-2.7.2.tar.gz -C /usr/local/ && \  
rm hadoop-2.7.2.tar.gz && \  
(cd /usr/local && ln -s hadoop-2.7.2 hadoop) && \  
rm -rf /usr/local/hadoop/share/doc  
  
ENV HADOOP_HOME /usr/local/hadoop  
ENV LD_LIBRARY_PATH /usr/local/hadoop/lib/native  

