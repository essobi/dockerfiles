FROM twistedogic/spark-hdfs-base  
MAINTAINER Jordan Li  
ENV HDFS_NAMENODE_ROOT_DIR /var/hdfs/namenode  
  
ADD conf/core-site.xml /etc/hadoop/etc/hadoop/core-site.xml  
ADD conf/hdfs-site.xml /etc/hadoop/etc/hadoop/hdfs-site.xml  
  
ADD start-hdfs-nn /usr/local/sbin/start-hdfs-nn  
  
VOLUME ["/var/hdfs/namenode"]  
COPY start.sh /  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 7077 8080 8020 50070  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

