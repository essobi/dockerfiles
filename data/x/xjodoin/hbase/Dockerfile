FROM java:8  
MAINTAINER Xavier Jodoin <xavier@jodoin.me>  
  
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
RUN mkdir /hbase-setup  
WORKDIR /hbase-setup  
  
ENV HBASE_VERSION 1.1.12  
ADD ./install-hbase.sh /hbase-setup/  
RUN ./install-hbase.sh  
  
RUN /opt/hbase/bin/hbase-config.sh  
  
ADD ./hbase-site.xml /opt/hbase/conf/hbase-site.xml  
  
ADD ./replace-hostname /opt/replace-hostname  
  
ADD start-pseudo-distributed.sh /opt/hbase/bin/start-pseudo-distributed.sh  
  
WORKDIR /opt/hbase/bin  
  
ENV PATH=$PATH:/opt/hbase/bin  
  
CMD /opt/hbase/bin/start-pseudo-distributed.sh  

