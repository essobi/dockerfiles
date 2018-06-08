FROM greatbsky/openjdkx:latest  
MAINTAINER architect.bian  
LABEL name="spark" license="MIT" build-date="20180126"  
  
ENV VERSION 2.2.1  
ENV SPARK_HOME /data/env/spark  
ENV SPARK_URL http://www.apache.org/dist/spark/spark-$VERSION//spark-$VERSION-
bin-hadoop2.7.tgz  
ENV PATH $PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin  
  
RUN yum update -y && cd /data/softs && wget "$SPARK_URL" && tar -zvxf
spark-$VERSION-bin-hadoop2.7.tgz && mv /data/softs/spark-$VERSION-bin-
hadoop2.7 /data/env/spark && rm -rf /data/softs/*  
  
CMD ["/data/env/spark/bin/spark-class",
"org.apache.spark.deploy.master.Master"]

