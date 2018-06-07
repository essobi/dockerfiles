# Cassandra Dockerfile  
FROM dockerfile/java:oracle-java6  
  
RUN \  
cd /tmp && \  
wget http://mirror.reverse.net/pub/apache/cassandra/1.2.19/apache-
cassandra-1.2.19-bin.tar.gz && \  
mv apache-cassandra-1.2.19-bin.tar.gz cassandra.tar.gz && \  
mkdir /tmp/cassandra && \  
tar xvzf cassandra.tar.gz -C /tmp/cassandra --strip-components=1 && \  
rm -f cassandra.tar.gz && \  
mv /tmp/cassandra /cassandra  
  
VOLUME ["/var/lib/cassandra", "/var/log/cassandra"]  
ENTRYPOINT ["/cassandra/bin/cassandra"]  
CMD ["-f"]  
EXPOSE 9160  

