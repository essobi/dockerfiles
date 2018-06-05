FROM develar/java:8u45  
  
MAINTAINER Petr Krebs, Avast  
  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
  
ENV FLUME_VERSION 1.6.0  
ENV FLUME_HOME /opt/lib/flume  
  
RUN mkdir -p /opt/lib && \  
wget -q http://www.eu.apache.org/dist/flume/$FLUME_VERSION/apache-
flume-$FLUME_VERSION-bin.tar.gz -O /opt/lib/apache-flume-$FLUME_VERSION-
bin.tar.gz && \  
tar xzf /opt/lib/apache-flume-$FLUME_VERSION-bin.tar.gz -C /opt/lib && \  
mv /opt/lib/apache-flume-$FLUME_VERSION-bin /opt/lib/flume && \  
rm /opt/lib/apache-flume-$FLUME_VERSION-bin.tar.gz && \  
mv $FLUME_HOME/conf/flume-conf.properties.template $FLUME_HOME/conf/flume-
conf.properties  
  
VOLUME [ "/opt/lib/flume/conf" ]  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENV HADOOP_VERSION=2.7.2  
ENV HADOOP_HOME=/opt/lib/hadoop-$HADOOP_VERSION  
  
RUN wget -q
http://www.eu.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz
-O /opt/lib/hadoop-$HADOOP_VERSION.tar.gz && \  
tar xzf /opt/lib/hadoop-$HADOOP_VERSION.tar.gz -C /opt/lib && \  
rm /opt/lib/hadoop-$HADOOP_VERSION.tar.gz  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

