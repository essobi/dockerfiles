FROM openjdk:8-jdk-alpine  
  
####################  
# Spark  
####################  
  
ENV SPARK_VERSION 2.0.0  
ENV HADOOP_VERSION_SHORT 2.7  
ENV SPARK_HOME /opt/spark  
ENV PATH $PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin  
  
RUN apk add --update --no-cache openssl openssh ca-certificates bash python
python3 py-pip procps  
  
RUN update-ca-certificates && \  
wget -q
https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-hadoop$HADOOP_VERSION_SHORT.tgz && \  
tar -zxf /spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION_SHORT.tgz && \  
rm /spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION_SHORT.tgz && \  
mkdir -p /opt && \  
mv spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION_SHORT /opt/spark && \  
mkdir -p /opt/spark/logs  
  
COPY conf $SPARK_HOME/conf  
  
VOLUME /opt/spark  
WORKDIR $SPARK_HOME  
EXPOSE 7077 8080  

