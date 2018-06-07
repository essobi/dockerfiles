FROM klustera/maven  
  
MAINTAINER Adolfo De Unánue <adolfo@klustera.com>  
  
  
## Variables de ambiente  
ENV FLUME_HOME /opt/flume  
ENV FLUME_VERSION=1.6.0  
ENV HADOOP_VERSION=2.7.2  
ENV HADOOP_HOME=/opt/hadoop  
ENV HADOOP_MIRROR="http://apache.osuosl.org"  
ENV HADOOP_DIST="hadoop-${HADOOP_VERSION}"  
ENV HADOOP_TARBALL="${HADOOP_DIST}.tar.gz"  
ENV
HADOOP_TARBALL_URL="$HADOOP_MIRROR/hadoop/common/$HADOOP_DIST/$HADOOP_TARBALL"  
## Apache Hadoop  
RUN mkdir -p "$HADOOP_HOME" && \  
wget -qO- $HADOOP_TARBALL_URL \  
| tar zxvf - -C $HADOOP_HOME \--strip 1  
  
## Conector de Hadoop para Google Cloud Storage (GCS)  
RUN wget https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-latest-
hadoop2.jar -P $HADOOP_HOME/share/hdfs  
  
## Ajustamos la configuración de Hadoop para leer/escribir de GCS  
ADD core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml  
ADD hadoop-env.sh $HADOOP_HOME/etc/hadoop/hadoop-env.sh  
  
## Apache Flume  
RUN mkdir /opt/flume  
RUN wget -qO- http://archive.apache.org/dist/flume/$FLUME_VERSION/apache-
flume-$FLUME_VERSION-bin.tar.gz \  
| tar zxvf - -C $FLUME_HOME \--strip 1  
  
ADD start-flume.sh $FLUME_HOME/bin/start-flume  
  
ADD *.conf /var/tmp/flume.conf  
  
EXPOSE 5140  
ENV PATH $FLUME_HOME/bin:$HADOOP_HOME/bin:$PATH  
  
CMD [ "start-flume" ]  

