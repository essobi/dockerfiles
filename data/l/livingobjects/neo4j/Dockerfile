FROM livingobjects/jre8:8u121_4  
  
ENV NEO4J_VERSION 2.3.6  
COPY neo4j /opt/neo4j_files/  
# Install Neo4j Community  
RUN wget --content-disposition
http://neo4j.com/artifact.php\?name\=neo4j-community-${NEO4J_VERSION}-unix.tar.gz
&& \  
mkdir -p /opt && \  
tar xvfz neo4j-community-${NEO4J_VERSION}-unix.tar.gz -C /opt && \  
ln -s /opt/neo4j-community-${NEO4J_VERSION} /opt/neo4j && \  
cp -vr /opt/neo4j_files/* /opt/neo4j-community-${NEO4J_VERSION}/ && \  
rm -rf neo4j-community-${NEO4J_VERSION}-unix.tar.gz /opt/neo4j_files/ && \  
  
# Chown all  
mkdir -p /opt/neo4j/logs/ && \  
chown lo-daemon. -R /opt/neo4j/  
  
# Install services  
ADD services /etc/sv  
  
# Expose access to Neo4j HTTP server  
EXPOSE 7474  
# Expose our data volumes  
VOLUME ["/opt/neo4j/data/graph.db", "/opt/neo4j/logs"]  

