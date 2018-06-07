FROM sequenceiq/hadoop-docker  
MAINTAINER SequenceIQ  
  
# hoya  
RUN curl -s
http://dffeaef8882d088c28ff-185c1feb8a981dddd593a05bb55b67aa.r18.cf1.rackcdn.com/hoya-0.13.1-all.tar.gz
| tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s hoya-0.13.1 hoya  
ENV HOYA_HOME /usr/local/hoya  
ENV PATH $PATH:$HOYA_HOME/bin  
  
# hbase  
RUN curl -so /usr/local/hbase-0.98.0.tar.gz
http://www.eu.apache.org/dist/hbase/hbase-0.98.0/hbase-0.98.0-hadoop2-bin.tar.gz  
RUN $BOOTSTRAP && $HADOOP_PREFIX/bin/hadoop dfsadmin -safemode leave &&
$HADOOP_PREFIX/bin/hdfs dfs -put /usr/local/hbase-0.98.0.tar.gz /hbase.tar.gz  
RUN mkdir /usr/local/hbaseconf  
ADD hadoop-metrics.properties /usr/local/hbaseconf/hadoop-metrics.properties  
ADD hbase-env.sh /usr/local/hbaseconf/hbase-env.sh  
ADD hbase-policy.xml /usr/local/hbaseconf/hbase-policy.xml  
ADD hbase-site.xml /usr/local/hbaseconf/hbase-site.xml  
ADD log4j.properties /usr/local/hbaseconf/log4j.properties  
  
# zookeeper  
RUN curl -s
http://xenia.sote.hu/ftp/mirrors/www.apache.org/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
| tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s zookeeper-3.4.6 zookeeper  
ENV ZOO_HOME /usr/local/zookeeper  
ENV PATH $PATH:$ZOO_HOME/bin  
RUN mv $ZOO_HOME/conf/zoo_sample.cfg $ZOO_HOME/conf/zoo.cfg  
RUN mkdir /tmp/zookeeper  
  
# add bootstrap-hoya  
ADD bootstrap-hoya.sh /etc/bootstrap-hoya.sh  
RUN chown root:root /etc/bootstrap-hoya.sh  
RUN chmod 700 /etc/bootstrap-hoya.sh  
  
CMD ["/etc/bootstrap-hoya.sh", "-d"]  
  
# start hbase cluster with 1 master and 1 region server  
# hoya create hbase --role master 1 --role worker 1 --manager localhost:8032
--filesystem hdfs://localhost:9000 --image hdfs://localhost:9000/hbase.tar.gz
--zkhosts localhost --appconf file:///usr/local/hbaseconf  

