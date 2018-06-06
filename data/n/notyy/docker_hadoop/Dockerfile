# mostly steal from sequenceiq's great Builderfile
https://registry.hub.docker.com/u/sequenceiq/hadoop-docker/dockerfile  
# adapt to ubuntu14.10  
FROM notyy/docker_hadoop:2.4.1_pseudo  
MAINTAINER notyycn <notyycn@gmail.com>  
  
# cluster master(namenode)  
RUN mkdir -p /var/hadoopdata/hdfs/nn  
RUN mkdir -p /var/hadoopdata/hdfs/dn  
  
ADD core-site.xml $HADOOP_PREFIX/etc/hadoop/core-site.xml  
ADD hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/hdfs-site.xml  
ADD mapred-site.xml $HADOOP_PREFIX/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml $HADOOP_PREFIX/etc/hadoop/yarn-site.xml  
  
WORKDIR /usr/local/hadoop  
  
ADD bootstrap.sh /etc/bootstrap.sh  
RUN chown root:root /etc/bootstrap.sh  
RUN chmod 700 /etc/bootstrap.sh  
  
ENV BOOTSTRAP /etc/bootstrap.sh  
  
CMD ["/etc/bootstrap.sh", "-dd"]  
  
EXPOSE 50020 50090 50070 50010 50075 8031 8032 8033 8040 8042 49707 22 8088
8030 9000  

