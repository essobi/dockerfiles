# HDFS Journalnode  
FROM f21global/hadoop-base:2.7.1  
MAINTAINER Francis Chuang <francis.chuang@boostport.com>  
  
RUN apt-get install hadoop-hdfs-journalnode --no-install-recommends -y  
  
ADD run-journalnode.sh /run-journalnode.sh  
  
VOLUME ["/var/lib/hadoop-hdfs/journal"]  
  
EXPOSE 8485 8480 8481  
CMD ["/run-journalnode.sh"]

