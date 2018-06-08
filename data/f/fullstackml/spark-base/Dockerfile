FROM fullstackml/debian-java:1.0  
MAINTAINER Dmitry Petrov <dmitry@fullstackml.com>  
  
LABEL com.fullstackml = "true" \  
com.fullstackml.function = "base-docker-images/spark-base" \  
com.fullstackml.version = "1.0"  
  
# Install Apache Spark  
RUN apt-get install -y ssh && \  
wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz
2>/dev/null && \  
tar zxf spark-2.0.0-bin-hadoop2.7.tgz -C /usr/local/ && \  
rm spark-2.0.0-bin-hadoop2.7.tgz && \  
(cd /usr/local && ln -s spark-2.0.0-bin-hadoop2.7 spark)  
  
ENV SPARK_HOME /usr/local/spark  

