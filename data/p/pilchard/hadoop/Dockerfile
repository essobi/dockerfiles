#  
# Author: pilchard  
FROM pilchard/java  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="CDH Dev"  
  
WORKDIR /  
  
RUN \  
yum install -y hadoop-hdfs-datanode hadoop-hdfs-journalnode.x86_64 hadoop-
hdfs-namenode.x86_64 hadoop-hdfs-nfs3.x86_64 hadoop-hdfs-nfs3.x86_64 hadoop-
hdfs-zkfc.x86_64 hadoop-httpfs.x86_64 \  
hadoop-mapreduce.x86_64 hadoop-yarn.x86_64 hadoop-hdfs-fuse.x86_64 hadoop-
mapreduce-historyserver.x86_64 \  
hadoop-yarn-nodemanager.x86_64 hadoop-yarn-proxyserver.x86_64 hadoop-yarn-
resourcemanager.x86_64 && \  
yum clean all  
  
CMD "/bin/bash"

