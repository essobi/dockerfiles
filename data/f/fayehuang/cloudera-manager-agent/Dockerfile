FROM fayehuang/centos-serf  
MAINTAINER FayeHuang  
#  
WORKDIR /docker_init/cm-agent  
ENV mysql_password=changeme  
RUN yum install -y ntp mysql-connector-java && yum clean all  
RUN mkdir -p /usr/lib/hive/lib/ && ln -s /usr/share/java/mysql-connector-
java.jar /usr/lib/hive/lib/mysql-connector-java.jar  
#  
ENV cm_version=5.4.3 cdh_version=5.4.4  
RUN wget http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-
cdh5.repo && mv cloudera-cdh5.repo /etc/yum.repos.d && \  
wget http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloudera-manager.repo
&& mv cloudera-manager.repo /etc/yum.repos.d && \  
sed -i.bak
s/^.*"baseurl".*/"baseurl=http:\/\/archive.cloudera.com\/cdh5\/redhat\/6\/x86_64\/cdh\/$cdh_version\/"/
/etc/yum.repos.d/cloudera-cdh5.repo && \  
sed -i.bak
s/^.*"baseurl".*/"baseurl=http:\/\/archive.cloudera.com\/cm5\/redhat\/6\/x86_64\/cm\/$cm_version\/"/
/etc/yum.repos.d/cloudera-manager.repo  
RUN yum install -y cloudera-manager-agent cloudera-manager-daemons
oracle-j2sdk1.7 \  
hadoop hadoop-httpfs \  
zookeeper zookeeper-server \  
hbase \  
hive hive-metastore hive-server2 hive-webhcat-server hive-hcatalog sentry \  
impala impala-server impala-state-store impala-catalog impala-shell llama
llama-master \  
oozie oozie-client \  
hue hue-plugins \  
pig \  
spark-core spark-worker spark-master spark-python spark-history-server \  
flume-ng flume-ng-agent \  
solr-server solr-crunch solr-mapreduce hbase-solr-indexer hbase-solr-doc hue-
search \  
sqoop \  
sqoop2-server sqoop2-client \  
mahout \  
&& yum clean all  
#  
COPY agent_init.sh agent_init.sh  
RUN chmod +x agent_init.sh  
ENV SERF_HOME /docker_init/serf  
COPY serf_init.sh $SERF_HOME/bin/serf_init.sh  
RUN chmod +x $SERF_HOME/bin/serf_init.sh  
  
COPY supervisord.conf /etc/supervisord.conf  
EXPOSE 22 50070 8088 8042 19888 3000  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

