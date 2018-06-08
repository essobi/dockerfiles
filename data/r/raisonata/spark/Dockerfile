# Raisonata Docker:  
# Spark 1.2.1, Scala 2.11.4  
FROM dockerfile/java:oracle-java8  
  
MAINTAINER Victor da Costa <victorockeiro@gmail.com>  
  
# Set environment Variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION 2.11.4  
ENV SPARK_VERSION 1.2.1  
ENV SBT_VERSION 0.13.6  
ENV SCALA_HOME /opt/scala-$SCALA_VERSION  
ENV SPARK_HOME /usr/share/scala/  
ENV SPARK_PID_DIR $SPARK_HOME/pid  
ENV PATH $SPARK_HOME:$SCALA_HOME/bin:$PATH  
  
# Common Scripting  
ADD scripts/spark-common.sh /usr/local/sbin/spark-common  
  
# Add DataStax sources  
ADD conf/datastax_key /tmp/datastax_key  
RUN apt-key add /tmp/datastax_key  
RUN echo "deb http://debian.datastax.com/community stable main" >
/etc/apt/sources.list.d/datastax.list  
  
# Install Scala  
RUN apt-get -y update  
RUN echo "Downloading http://www.scala-
lang.org/files/archive/scala-$SCALA_VERSION.deb"  
ADD http://www.scala-lang.org/files/archive/scala-$SCALA_VERSION.deb /tmp/  
RUN dpkg -i /tmp/scala-$SCALA_VERSION.deb  
RUN apt-get -y -f install  
RUN rm -rf /tmp/scala-$SCALA_VERSION.deb  
  
# Install SBT  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a
/etc/apt/sources.list.d/sbt.list  
sudo apt-get update  
sudo apt-get -y install sbt  
  
# Install Spark  
RUN echo "Donwloading
http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-hadoop2.4.tgz"  
ADD http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-
hadoop2.4.tgz /tmp/  
RUN (cd /tmp && gunzip < spark-${SPARK_VERSION}-bin-hadoop2.4.tgz)|(cd /opt &&
tar -xvf -)  
RUN ln -s /opt/spark-$SPARK_VERSION-bin-hadoop2.4 /opt/spark  
RUN rm /tmp/spark-$SPARK_VERSION-bin-hadoop2.4.tgz  
  
# Configure Spark  
ADD conf/spark-defaults.conf /opt/spark/conf/  
  
VOLUME ["/store"]  
CMD [""]

