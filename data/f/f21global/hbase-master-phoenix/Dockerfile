# HBase master with phoenix  
  
FROM f21global/hbase-master:1.1.4  
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
&& mv /opt/phoenix/phoenix-$PHOENIX_VER-HBase-$HBASE_MAJOR_VER-client-without-
hbase.jar /opt/hbase/lib/ \  
&& mv /opt/phoenix/bin/tephra /opt/hbase/bin/tephra \  
&& mv /opt/phoenix/bin/tephra-env.sh /opt/hbase/bin/tephra-env.sh \  
&& rm -rf /opt/phoenix  
  
ADD run-master.sh /run-phoenix-master.sh  
  
EXPOSE 16010 16020 16030  
  
CMD ["/run-phoenix-master.sh"]

