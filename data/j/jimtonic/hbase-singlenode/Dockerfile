FROM ubuntu:trusty  
  
MAINTAINER Ferdinand Rewicki <ferdi@glasspod.de>  
  
# install java jdk 8 and other tools  
RUN apt-get update && \  
apt-get install -y openjdk-7-jre wget vim bash tar  
  
ENV HBASE_VERSION 1.2.4  
WORKDIR /opt  
RUN wget
http://archive.apache.org/dist/hbase/${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz
\  
&& tar xzvf hbase-${HBASE_VERSION}-bin.tar.gz \  
&& rm hbase-${HBASE_VERSION}-bin.tar.gz \  
&& mv hbase-${HBASE_VERSION} hbase  
  
ADD files/hbase-site.xml /opt/hbase/conf  
ADD files/hbase-env.sh /opt/hbase/conf  
RUN chmod +x /opt/hbase/conf/hbase-env.sh  
  
EXPOSE 9000  
# REST API  
EXPOSE 8080  
# REST Web UI at :8085/rest.jsp  
EXPOSE 8085  
# Thrift API  
EXPOSE 9090  
# Thrift Web UI at :9095/thrift.jsp  
EXPOSE 9095  
# HBase's Embedded zookeeper cluster  
EXPOSE 2181  
# HBase Master web UI at :16010/master-status; ZK at :16010/zk.jsp  
EXPOSE 16010  
CMD ["/opt/hbase/bin/hbase", "master", "start"]  

