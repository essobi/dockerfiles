FROM tairangroup/hadoop:latest  
MAINTAINER ztzjut <i@sunisle.org>  
  
# Setup env  
ENV HBASE_HOME /opt/hbase  
ENV PATH $HBASE_HOME/bin:$PATH  
ENV KEEP false  
  
RUN echo "export HBASE_HOME=/opt/hbase" >> /etc/profile  
RUN echo "export PATH=$HBASE_HOME/bin:$PATH" >> /etc/profile  
  
# Download hbase  
RUN wget -q -O -
http://mirrors.hust.edu.cn/apache/hbase/1.3.1/hbase-1.3.1-bin.tar.gz | tar
-xzf - -C /opt/ \  
&& mv /opt/hbase-1.3.1 /opt/hbase  
  
COPY hbase-env.sh $HBASE_HOME/conf/  
COPY hbase-site.xml $HBASE_HOME/conf/  
  
# Download phoenix  
RUN wget -q -O - https://mirrors.tuna.tsinghua.edu.cn/apache/phoenix/apache-
phoenix-4.13.1-HBase-1.3/bin/apache-phoenix-4.13.1-HBase-1.3-bin.tar.gz | tar
-xzf - -C /opt/ \  
&& mv /opt/apache-phoenix-4.13.1-HBase-1.3-bin /opt/phoenix  
  
RUN cp /opt/phoenix/phoenix-4.13.1-HBase-1.3-server.jar /opt/hbase/lib  
  
COPY hbase-site.xml.phoenix /opt/phoenix/bin/hbase-site.xml  
  
COPY bootstrap_hbase.sh /bin/bootstrap_hbase.sh  
COPY bootstrap.sh /bin/bootstrap.sh  
  
RUN chmod +x /bin/bootstrap*  
  
EXPOSE 60000 60010 60030  
ENTRYPOINT /bin/bootstrap.sh $KEEP  

