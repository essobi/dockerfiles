FROM athlinks/confluent-base  
  
ADD conf/zookeeper.properties /opt/confluent/etc/kafka/zookeeper.properties  
ADD bin/entrypoint.sh /usr/local/bin/  
  
EXPOSE 2181 2888 3888  
CMD ["/opt/confluent/bin/zookeeper-server-start",
"/opt/confluent/etc/kafka/zookeeper.properties"]  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

