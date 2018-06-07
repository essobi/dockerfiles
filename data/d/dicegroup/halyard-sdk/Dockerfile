FROM bde2020/hadoop-base:2.0.0-hadoop2.7.4-java8 as hadoop-base  
FROM bde2020/hbase-base:1.0.0-hbase1.2.6 as hbase-base  
  
FROM openjdk:8  
MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>  
  
ENV HADOOP_VERSION=2.7.4  
COPY \--from=hadoop-base /opt/hadoop-$HADOOP_VERSION
/opt/hadoop-$HADOOP_VERSION  
RUN ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop  
ENV PATH /opt/hadoop-$HADOOP_VERSION/bin:$PATH  
  
ENV HBASE_VERSION=1.2.6  
COPY \--from=hbase-base /opt/hbase-$HBASE_VERSION /opt/hbase-$HBASE_VERSION  
RUN ln -s /opt/hbase-$HBASE_VERSION/conf /etc/hbase  
ENV PATH /opt/hbase-$HBASE_VERSION/bin:$PATH  
  
ENV HALYARD_VERSION 1.2  
ENV HALYARD_URL
https://github.com/Merck/Halyard/releases/download/r$HALYARD_VERSION/halyard-
sdk-$HALYARD_VERSION.zip  
RUN set -x \  
&& curl -fSL "$HALYARD_URL" -o /tmp/halyard-sdk.zip \  
&& mkdir /opt/halyard-$HALYARD_VERSION \  
&& unzip /tmp/halyard-sdk.zip -d /opt/halyard-$HALYARD_VERSION/ \  
&& rm /tmp/halyard-sdk.zip*  
  
ENV HALYARD_PREFIX=/opt/halyard-$HALYARD_VERSION  
  
ENV USER=root  
ENV PATH $HALYARD_PREFIX:$PATH  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
WORKDIR $HALYARD_PREFIX  
  
ENTRYPOINT ["/entrypoint.sh"]  

