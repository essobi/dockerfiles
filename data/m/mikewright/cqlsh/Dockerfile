FROM ubuntu:14.04  
MAINTAINER mkwright@gmail.com  
  
RUN apt-get update && \  
apt-get install -y python curl && \  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
RUN curl -sSL -o /cassandra.tar.gz
http://apache.claz.org/cassandra/2.1.15/apache-cassandra-2.1.15-bin.tar.gz &&
\  
tar -xvf cassandra.tar.gz && \  
mv apache-cassandra-2.1.15 cassandra && \  
rm /cassandra.tar.gz  
  
ENTRYPOINT ["/cassandra/bin/cqlsh"]  

