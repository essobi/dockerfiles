FROM qnib/d-java6:wheezy  
  
ADD etc/apt/sources.list.d/cloudera.list /etc/apt/sources.list.d/  
RUN curl -s archive.key
http://archive.cloudera.com/cdh5/debian/wheezy/amd64/cdh/archive.key | apt-key
add - && \  
apt-get update  
  
# Carve this out for different host types  
## JobTracker host  
RUN apt-get install -y hadoop-0.20-mapreduce-jobtracker  
## NameNode  
RUN apt-get install -y hadoop-hdfs-namenode  
## ??  
RUN apt-get install -y hadoop-0.20-mapreduce-tasktracker hadoop-hdfs-datanode  
  
## Configure HDFS  
RUN rm -f /etc/hadoop/conf  
ADD etc/hadoop/*.xml /etc/hadoop/conf/  
  
## Startscript - namenode  
ADD opt/qnib/hdfs/namenode/bin/start.sh /opt/qnib/hdfs/namenode/bin/  
ADD etc/supervisord.d/hdfs-namenode.ini /etc/supervisord.d/  
## Startscript - datanode  
ADD opt/qnib/hdfs/datanode/bin/start.sh /opt/qnib/hdfs/datanode/bin/  
ADD etc/supervisord.d/hdfs-datanode.ini /etc/supervisord.d/  

