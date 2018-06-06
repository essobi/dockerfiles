from sequenceiq/hadoop-docker:2.7.0  
VOLUME /input  
  
ADD hdfs-dfs-client.sh /hdfs-dfs-client.sh  
  
RUN chmod a+rwx /usr/local/hadoop/etc/hadoop/  
  
ENTRYPOINT ["/hdfs-dfs-client.sh"]  
CMD []  

