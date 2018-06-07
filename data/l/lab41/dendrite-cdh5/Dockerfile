FROM lab41/dendrite-java  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
# cdh5 package, key, and repo  
ADD cdh5-repository_1.0_all.deb cdh5-repository_1.0_all.deb  
RUN dpkg -i cdh5-repository_1.0_all.deb  
RUN curl -s
http://archive.cloudera.com/cdh5/ubuntu/precise/amd64/cdh/archive.key | apt-
key add -  
RUN echo "deb [arch=amd64]
http://archive.cloudera.com/cdh5/ubuntu/precise/amd64/cdh precise-cdh5
contrib\ndeb-src http://archive.cloudera.com/cdh5/ubuntu/precise/amd64/cdh
precise-cdh5 contrib" > /etc/apt/sources.list.d/cloudera.list  
  
RUN apt-get update  
RUN apt-get install -y hadoop-hdfs-datanode \  
hadoop-hdfs-namenode \  
hadoop-mapreduce \  
hadoop-mapreduce-historyserver \  
hadoop-yarn-nodemanager \  
hadoop-yarn-proxyserver \  
hadoop-yarn-resourcemanager \  
hbase-master \  
hbase-regionserver \  
zookeeper \  
zookeeper-server  
# zookeeper  
RUN service zookeeper-server init  
ADD zookeeper.conf /etc/supervisor/conf.d/zookeeper.conf  
  
# hdfs supervisor  
ADD hadoop-hdfs-namenode.conf /etc/supervisor/conf.d/hadoop-hdfs-namenode.conf  
ADD hadoop-hdfs-datanode.conf /etc/supervisor/conf.d/hadoop-hdfs-datanode.conf  
  
# yarn  
ADD hadoop-mapreduce.conf /etc/supervisor/conf.d/hadoop-mapreduce.conf  
ADD hadoop-yarn-nodemanager.conf /etc/supervisor/conf.d/hadoop-yarn-
nodemanager.conf  
ADD hadoop-yarn-resourcemanager.conf /etc/supervisor/conf.d/hadoop-yarn-
resourcemanager.conf  
RUN sed -i
's|</configuration>|<property><name>yarn.nodemanager.resource.memory-
mb</name><value>8192</value></property></configuration>|'
/etc/hadoop/conf/yarn-site.xml; \  
sed -i 's|JAVA_HEAP_MAX=-Xmx1000m|JAVA_HEAP_MAX=-Xmx8192m|'
/etc/hadoop/conf/yarn-env.sh  
  
# hbase  
ADD hbase-master.conf /etc/supervisor/conf.d/hbase-master.conf  
ADD hbase-regionserver.conf /etc/supervisor/conf.d/hbase-regionserver.conf  
RUN echo 'export JAVA_HOME=/usr/lib/jvm/jdk1.7.0_51' >> /etc/hbase/conf/hbase-
env.sh; \  
sed -i
's|<configuration>|<configuration><property><name>hbase.cluster.distributed</name><value>true</value></property><property><name>hbase.rootdir</name><value>hdfs://localhost:54310/hbase</value></property>|'
/etc/hbase/conf/hbase-site.xml  
  
# add hdfs config  
RUN sed -i
's|<configuration>|<configuration><property><name>fs.default.name</name><value>hdfs://localhost:54310/</value><description>.</description></property>|'
/etc/hadoop/conf/core-site.xml  
  
# format hdfs  
RUN su -c "hadoop namenode -format" \- hdfs  
RUN service hadoop-hdfs-namenode start; \  
service hadoop-hdfs-datanode start; \  
su -c "hadoop fs -mkdir /user" \- hdfs; \  
su -c "hadoop fs -mkdir /user/root" \- hdfs; \  
su -c "hadoop fs -mkdir /user/root/dendrite" \- hdfs; \  
su -c "hadoop fs -chown -R root:root /user/root" \- hdfs; \  
su -c "hadoop fs -mkdir /tmp" \- hdfs; \  
su -c "hadoop fs -mkdir /hbase" \- hdfs; \  
su -c "hadoop fs -chown hbase /hbase" \- hdfs; \  
su -c "hadoop fs -chmod -R 777 /tmp" \- hdfs; \  
su -c "hadoop fs -mkdir /user/tomcat7" \- hdfs; \  
su -c "hadoop fs -chown -R tomcat7 /user/tomcat7" \- hdfs; \  
su -c "hadoop fs -chmod -R 777 /user/tomcat7" \- hdfs  

