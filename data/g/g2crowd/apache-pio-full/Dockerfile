from debian:8.8  
ENV BASEDIR /pio  
  
RUN mkdir $BASEDIR  
  
WORKDIR $BASEDIR  
  
RUN apt-get update && apt-get install -y wget  
  
RUN wget
http://mirrors.ibiblio.org/apache/incubator/predictionio/0.11.0-incubating/apache-
predictionio-0.11.0-incubating.tar.gz  
  
RUN tar -xvf *.tar.gz  
  
RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get -t jessie-backports install -y openjdk-8-jdk  
  
RUN ./make-distribution.sh  
  
RUN tar -xvf PredictionIO-*.tar.gz  
  
ENV PIO_ROOT /PredictionIO-compiled  
  
RUN mv $(find `pwd` -maxdepth 1 -type d -name "PredictionIO*") $PIO_ROOT  
  
WORKDIR $PIO_ROOT  
  
RUN mkdir $PIO_ROOT/vendors  
  
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.3-bin-hadoop2.6.tgz  
  
RUN tar zxvfC spark-1.6.3-bin-hadoop2.6.tgz $PIO_ROOT/vendors  
  
RUN wget
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.6.tar.gz  
  
RUN tar zxvfC elasticsearch-1.7.6.tar.gz $PIO_ROOT/vendors  
  
RUN wget http://mirror.nexcess.net/apache/hbase/1.2.5/hbase-1.2.5-bin.tar.gz  
  
RUN tar zxvfC hbase-1.2.5-bin.tar.gz $PIO_ROOT/vendors  
  
COPY hbase-site.xml $PIO_ROOT/vendors/hbase-1.2.5/conf/hbase-site.xml  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
COPY pio-env.sh $PIO_ROOT/conf/pio-env.sh  
  
RUN apt-get update && apt-get install -y git  
  
ENV PIO_HOME $PIO_ROOT  

