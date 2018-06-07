# HBase regionserver with phoenix  
FROM f21global/hbase-regionserver:1.1.4  
MAINTAINER Francis Chuang <francis.chuang@boostport.com>  
  
ENV HBASE_MAJOR_VER 1.1  
ENV PHOENIX_VER 4.7.0  
RUN mkdir -p /opt/phoenix \  
&& wget -q -O -
http://apache.uberglobalmirror.com/phoenix/phoenix-$PHOENIX_VER-
HBase-$HBASE_MAJOR_VER/bin/phoenix-$PHOENIX_VER-HBase-$HBASE_MAJOR_VER-
bin.tar.gz | tar -xzf - -C /opt/phoenix --strip-components 1 \  
&& chown -R hbase:hadoop /opt/phoenix \  
&& mv /opt/phoenix/phoenix-$PHOENIX_VER-HBase-$HBASE_MAJOR_VER-server.jar
/opt/hbase/lib/ \  
&& rm -rf /opt/phoenix  
  
ADD run-regionserver.sh /run-phoenix-regionserver.sh  
  
EXPOSE 16020 16030  
CMD ["/run-phoenix-regionserver.sh"]

