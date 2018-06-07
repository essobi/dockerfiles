FROM isthari/cdh5-base  
  
RUN apt-get update  
RUN apt-get install -y -t jessie-cdh5 hadoop-mapreduce hive-server2  
RUN apt-get install -y vim  
ADD core-site.xml /etc/hadoop/conf/core-site.xml  
ADD yarn-site.xml /etc/hadoop/conf/yarn-site.xml  
ADD hive-site.xml /usr/lib/hive/conf  
ADD start.sh /root/start.sh  
RUN chmod u+x /root/start.sh  
RUN echo "export HADOOP_MAPRED_HOME=/usr/lib/hadoop-mapreduce" >>
/etc/default/hive-server2  
RUN echo "192.168.4.134 hdfs-namenode" >> /etc/hosts  
  
EXPOSE 10000  
CMD /root/start.sh  

