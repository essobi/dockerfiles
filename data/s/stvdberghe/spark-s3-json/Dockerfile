FROM ubuntu:latest  
MAINTAINER Steven <steven.vandenberghe@sirris.be>  
  
#install packages  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends openjdk-8-jdk-headless wget python3
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/  
  
#install tini  
RUN wget https://github.com/krallin/tini/releases/download/v0.10.0/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
#build spark  
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0.tgz && tar xvzf
spark-2.0.0.tgz  
WORKDIR spark-2.0.0  
RUN ./dev/make-distribution.sh --name spark-swift -Phadoop-2.7 -Pyarn -Phive
-Phive-thriftserver  
WORKDIR dist/jars  
RUN wget http://www.congiu.net/hive-json-serde/1.3.7/cdh5/json-
serde-1.3.7-jar-with-dependencies.jar  
RUN wget http://central.maven.org/maven2/org/apache/hadoop/hadoop-
aws/2.7.3/hadoop-aws-2.7.3.jar
http://central.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-
sdk-1.7.4.jar  
WORKDIR /spark-2.0.0/dist  
COPY spark-defaults.conf conf/  
#ready  
ENV PYSPARK_PYTHON=/usr/bin/python3  
ENV PYSPARK_PYTHON=python3  
ENV SPARK_HOME=/spark-2.0.0/dist  
CMD ["./bin/spark-class", "org.apache.spark.deploy.master.Master"]  
  

