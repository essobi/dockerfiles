FROM dockerfile/java:oracle-java8  
MAINTAINER Cogniteev <tech@cogniteev.com>  
  
RUN groupadd -r hbase && useradd -m -r -g hbase hbase  
USER hbase  
  
RUN cd /home/hbase && \  
wget -O - -q \  
http://apache.mesi.com.ar/hbase/hbase-0.98.10/hbase-0.98.10-hadoop2-bin.tar.gz
\  
| tar --strip-components=1 -zxf -  
  
ADD ./conf/ /home/hbase/conf/  
WORKDIR /home/hbase  
  
# zookeeper  
EXPOSE 2181  
# HBase Master API port  
EXPOSE 60000  
# HBase Master Web UI  
EXPOSE 60010  
# Regionserver API port  
EXPOSE 60020  
# HBase Regionserver web UI  
EXPOSE 60030  
CMD /home/hbase/bin/hbase master start  

