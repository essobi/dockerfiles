# HDFS Namenode  
FROM f21global/hadoop-base:2.7.1  
MAINTAINER Francis Chuang <francis.chuang@boostport.com>  
  
RUN apt-get install hadoop-hdfs-namenode hadoop-hdfs-zkfc hadoop-client --no-
install-recommends -y  
  
ADD run-namenode.sh /run-namenode.sh  
  
VOLUME ["/var/lib/hadoop-hdfs/cache/hdfs/dfs/name"]  
  
EXPOSE 8020 9000 50070 50470  
CMD ["/run-namenode.sh"]

