# HDFS Datanode  
FROM f21global/hadoop-base:2.7.1  
MAINTAINER Francis Chuang <francis.chuang@boostport.com>  
  
RUN apt-get install hadoop-hdfs-datanode --no-install-recommends -y  
  
ADD run-datanode.sh /run-datanode.sh  
  
VOLUME ["/var/lib/hadoop-hdfs/data"]  
  
EXPOSE 50010 50075 50475 1006 50020  
CMD ["/run-datanode.sh"]

