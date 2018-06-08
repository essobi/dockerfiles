FROM lucitec/base-java8  
  
RUN apt-get update  
RUN apt-get install -y wget  
  
ENV CASSANDRA_HOME /opt/cassandra  
  
RUN mkdir -p /data/data /data/commitlog /data/saved_caches /logs /init
$CASSANDRA_HOME  
RUN wget --no-check-certificate --progress=dot:mega -O -
ftp://gd.tuwien.ac.at/pub/infosys/servers/http/apache/dist/cassandra/2.0.10/apache-
cassandra-2.0.10-bin.tar.gz | tar -zx -C $CASSANDRA_HOME \--strip-components=1  
RUN ln -s /usr/share/java/jna.jar $CASSANDRA_HOME/lib/  
  
EXPOSE 7000 7001 7199 9160 9042  
ADD cassandra.yaml $CASSANDRA_HOME/conf/cassandra.yaml  
ADD cassandra-env.sh $CASSANDRA_HOME/conf/cassandra-env.sh  
ADD log4j-server.properties $CASSANDRA_HOME/conf/log4j-server.properties  
ADD start.sh $CASSANDRA_HOME/bin/start.sh  
ADD cassandra-topology.properties $CASSANDRA_HOME/conf/cassandra-
topology.properties  
  
CMD "$CASSANDRA_HOME/bin/start.sh"

