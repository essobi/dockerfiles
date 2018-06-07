FROM java:8-jdk  
  
MAINTAINER Bolesław Tekielski <bolek@vault13.pl>  
  
ENV SPARK_VERSION 1.6.1  
ENV HADOOP_VERSION 2.6  
ENV JODA_TIME_VERSION 2.8.2  
ENV SPARK_PACKAGE spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz  
ENV SPARK_HOME /opt/spark/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION  
ENV PATH $PATH:$SPARK_HOME/bin  
  
RUN mkdir -p $SPARK_HOME \  
&& wget http://www-
eu.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-
hadoop$HADOOP_VERSION.tgz -O - \  
| tar xz -C /opt/spark  
  
RUN wget -O $SPARK_HOME/lib/joda-time-$JODA_TIME_VERSION.jar \  
http://central.maven.org/maven2/joda-time/joda-time/$JODA_TIME_VERSION/joda-
time-$JODA_TIME_VERSION.jar  
  
WORKDIR $SPARK_HOME  
  
ENTRYPOINT ["spark-shell"]  
  
CMD ["--name", "INSTANT_SPARK"]

