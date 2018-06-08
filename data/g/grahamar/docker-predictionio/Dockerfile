FROM ubuntu  
MAINTAINER Fabian M. Borschel <fabian.borschel@commercetools.de>  
  
ENV PIO_VERSION 0.9.6  
ENV SPARK_VERSION 1.6.1  
ENV ELASTICSEARCH_VERSION 2.3.2  
ENV HBASE_VERSION 1.1.4  
  
ENV PIO_HOME /PredictionIO-$PIO_VERSION  
ENV PATH=$PIO_HOME/bin:$PATH  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN apt-get update && apt-get install -y curl openjdk-8-jdk libgfortran3
python-pip && \  
pip install predictionio  
  
RUN curl -O
https://d8k1yxp8elc6b.cloudfront.net/PredictionIO-$PIO_VERSION.tar.gz && \  
tar -xvzf PredictionIO-$PIO_VERSION.tar.gz -C / && mkdir -p $PIO_HOME/vendors
&& \  
rm PredictionIO-$PIO_VERSION.tar.gz  
  
ADD files/pio-env.sh $PIO_HOME/conf/pio-env.sh  
  
RUN curl -O http://d3kbcqa49mib13.cloudfront.net/spark-$SPARK_VERSION-bin-
hadoop2.6.tgz && \  
tar -xvzf spark-$SPARK_VERSION-bin-hadoop2.6.tgz -C $PIO_HOME/vendors && \  
rm spark-$SPARK_VERSION-bin-hadoop2.6.tgz  
  
RUN curl -L -O
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$ELASTICSEARCH_VERSION/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz
&& \  
tar -xvzf elasticsearch-$ELASTICSEARCH_VERSION.tar.gz -C $PIO_HOME/vendors &&
\  
rm elasticsearch-$ELASTICSEARCH_VERSION.tar.gz && \  
echo 'cluster.name: predictionio' >>
$PIO_HOME/vendors/elasticsearch-$ELASTICSEARCH_VERSION/config/elasticsearch.yml
&& \  
echo 'network.host: 127.0.0.1' >>
$PIO_HOME/vendors/elasticsearch-$ELASTICSEARCH_VERSION/config/elasticsearch.yml  
  
RUN curl -O
http://archive.apache.org/dist/hbase/$HBASE_VERSION/hbase-$HBASE_VERSION-
bin.tar.gz && \  
tar -xvzf hbase-$HBASE_VERSION-bin.tar.gz -C $PIO_HOME/vendors && \  
rm hbase-$HBASE_VERSION-bin.tar.gz  
  
ADD files/hbase-site.xml $PIO_HOME/vendors/hbase-$HBASE_VERSION/conf/hbase-
site.xml  
  
RUN sed -i "s|VAR_PIO_HOME|$PIO_HOME|"
$PIO_HOME/vendors/hbase-$HBASE_VERSION/conf/hbase-site.xml && \  
sed -i "s|VAR_HBASE_VERSION|$HBASE_VERSION|"
$PIO_HOME/vendors/hbase-$HBASE_VERSION/conf/hbase-site.xml  
#triggers fetching the complete sbt environment  
RUN $PIO_HOME/sbt/sbt -batch  
  
RUN useradd -c 'PredictionIO user' -m -d /home/predictionio -s /bin/bash
predictionio && \  
chown -R predictionio.predictionio $PIO_HOME  

