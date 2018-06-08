FROM develar/java  
MAINTAINER Oleg Fedoseev <oleg.fedoseev@me.com>  
  
ENV HBASE_VERSION 1.2.2  
ENV HBASE_HOME /usr/local/hbase  
ENV HBASE_CONF_DIR /usr/local/hbase/conf  
ENV HBASE_LOG_DIR /data/logs  
ENV HBASE_MANAGES_ZK true  
ENV HBASE_IDENT_STRING docker  
  
ENV PATH $PATH:$HBASE_HOME/bin:$HBASE_HOME/sbin  
  
RUN apk add --update curl bash && \  
curl -kL http://www-eu.apache.org/dist/hbase/stable/hbase-$HBASE_VERSION-
bin.tar.gz | tar -zx -C /tmp && \  
mv /tmp/hbase-$HBASE_VERSION /usr/local/hbase && apk del curl && \  
rm -rf /tmp/* /var/cache/apk/* $HBASE_HOME/bin/*.cmd /usr/local/hbase/docs  
  
ADD hbase-site.xml $HBASE_HOME/conf/hbase-site.xml  
ADD entrypoint.sh $HBASE_HOME/bin/entrypoint.sh  
  
VOLUME /data  
  
# REST API  
EXPOSE 8080  
# REST Web UI  
EXPOSE 8085  
# Thrift API  
EXPOSE 9090  
# Thrift Web UI  
EXPOSE 9095  
# HBase Master  
EXPOSE 16000  
# HBase Master web UI  
EXPOSE 16010  
# HBase RegionServer  
EXPOSE 16020  
# HBase RegionServer web UI  
EXPOSE 16030  
# ZooKeeper  
EXPOSE 2181  
ENTRYPOINT ["/usr/local/hbase/bin/entrypoint.sh"]  

