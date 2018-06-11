FROM google/debian:wheezy  
MAINTAINER Jordan Li <twistedogic@gmail.com>  
ENV SCALA_VERSION 2.10.3  
ENV SPARK_VERSION 1.4.1  
ENV SPARK_TGZ spark-1.4.1-bin-hadoop2.6  
ENV SPARK_DOWNLOAD_URL http://d3kbcqa49mib13.cloudfront.net/spark-1.4.1-bin-
hadoop2.6.tgz  
ENV SCALA_HOME /opt/scala-$SCALA_VERSION  
ENV SPARK_HOME /opt/spark-$SPARK_VERSION  
ENV PATH $SPARK_HOME:$SCALA_HOME/bin:$PATH  
ENV SERF_HOME /root/serf  
RUN mkdir $SERF_HOME && mkdir $SERF_HOME/bin && mkdir $SERF_HOME/etc  
WORKDIR /  
  
RUN apt-get update && apt-get install wget unzip supervisor ca-certificates
openjdk-7-jre supervisor python2.7 -y  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
# Install Scala  
RUN wget http://www.scala-lang.org/files/archive/scala-$SCALA_VERSION.tgz -P /  
RUN (cd / && gunzip < scala-$SCALA_VERSION.tgz)|(cd /opt && tar -xvf -)  
RUN rm /scala-$SCALA_VERSION.tgz  
  
# Install Spark  
RUN wget "${SPARK_DOWNLOAD_URL}" -P /  
RUN (cd / && gunzip < ${SPARK_TGZ}.tgz)|(cd /opt && tar -xvf -)  
RUN (ln -s /opt/${SPARK_TGZ} /opt/spark-$SPARK_VERSION && rm
/${SPARK_TGZ}.tgz)  
  
# Install Serf  
RUN wget --no-check-certificate
https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip -P /tmp  
RUN unzip /tmp/0.6.4_linux_amd64.zip -d $SERF_HOME/bin && rm -f
/tmp/0.6.4_linux_amd64.zip  
  
COPY serf_init.sh $SERF_HOME/bin/serf_init.sh  
COPY updatehosts.json $SERF_HOME/etc/updatehosts.json  
COPY updatehosts.sh $SERF_HOME/bin/updatehosts.sh  
RUN chmod +x $SERF_HOME/bin/*  
  

