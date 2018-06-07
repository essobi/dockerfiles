FROM cassandra:2.1.8  
# Install cUrl: needed to download and install Stratio/cassandra-lucene-index  
RUN apt-get update && apt-get install -y curl  
  
# Install Stratio/cassandra-lucene-index from Maven central  
RUN cd /usr/share/cassandra/lib && \  
curl -LO
http://search.maven.org/remotecontent?filepath=com/stratio/cassandra/cassandra-
lucene-index-plugin/2.1.8.2/cassandra-lucene-index-plugin-2.1.8.2.jar  

