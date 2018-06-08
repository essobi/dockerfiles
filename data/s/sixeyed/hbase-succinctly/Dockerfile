FROM sixeyed/hadoop-succinctly:2.7.2  
MAINTAINER Elton Stoneman <elton@sixeyed.com>  
  
ENV HBASE_HOME=/opt/hbase  
  
RUN mkdir /hbase-setup  
WORKDIR /hbase-setup  
  
ADD install-hbase.sh /hbase-setup/  
RUN chmod +x ./install-hbase.sh  
RUN ./install-hbase.sh  
  
ADD hbase-site.xml /opt/hbase/conf/hbase-site.xml  
ADD start-hbase-all.sh /opt/hbase/bin/start-hbase-all.sh  
RUN chmod +x /opt/hbase/bin/start-hbase-all.sh  
  
ADD setup-hdfs.sh /hbase-setup/  
RUN chmod +x ./setup-hdfs.sh  
RUN ./setup-hdfs.sh  
  
RUN mkdir /tmp/sample-data  
ADD ./sample-data/ /tmp/sample-data/  
  
# Servers  
EXPOSE 60000  
EXPOSE 60020  
EXPOSE 2181  
# APIs  
EXPOSE 8080  
EXPOSE 9090  
# Web UIs  
EXPOSE 60010  
EXPOSE 60030  
EXPOSE 8085  
EXPOSE 9095  
WORKDIR /opt/hbase/bin  
  
ENV PATH=$PATH:/opt/hbase/bin  
  
# run in pseudo-distributed mode with Stargate & Thrift:  
CMD /opt/hbase/bin/start-hbase-all.sh  

