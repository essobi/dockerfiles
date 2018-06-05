FROM ubuntu  
  
RUN apt-get update && \  
apt-get -y install gcc make flex bison byacc git curl openjdk-7-jdk  
  
#Install Spark 1.6  
ENV SPARK_VERSION 1.6.0-bin-hadoop2.6  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}.tgz |
tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s spark-$SPARK_VERSION spark  
ENV SPARK_HOME /usr/local/spark  
ENV PATH $SPARK_HOME/bin:$PATH  
  
RUN git clone https://github.com/davies/tpcds-kit.git && \  
cd tpcds-kit/tools/ && \  
make -f Makefile.suite  
  
#This part is pretty silly but needed for packaging spark-sql-perf  
ENV DBC_USERNAME foo  
ENV DBC_PASSWORD bar  
ENV DBC_URL buzz  
  
RUN git clone https://github.com/databricks/spark-sql-perf.git && \  
cd spark-sql-perf && \  
build/sbt package  
  
ADD setup.scala .  
  
RUN spark-shell -i setup.scala --jars /spark-sql-perf/target/scala-2.10/spark-
sql-perf*.jar  
  
CMD spark-shell

