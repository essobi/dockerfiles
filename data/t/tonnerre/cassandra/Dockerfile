FROM cassandra:3  
RUN sed -i -e 's/^partitioner:
org.apache.cassandra.dht.Murmur3Partitioner$/partitioner:
org.apache.cassandra.dht.ByteOrderedPartitioner/'
/etc/cassandra/cassandra.yaml  
RUN echo
-Dcassandra.partitioner=org.apache.cassandra.dht.ByteOrderedPartitioner >>
/etc/cassandra/jvm.options  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["cassandra", "-f"]  

