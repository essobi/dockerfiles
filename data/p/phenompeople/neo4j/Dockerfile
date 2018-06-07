FROM phenompeople/centos-sunjre  
ENV NEO4J_VERSION=3.2.6  
EXPOSE 7474 7473 7687  
RUN wget -q -O /tmp/neo4j.tar.gz
"http://dist.neo4j.org/neo4j-community-${NEO4J_VERSION}-unix.tar.gz" && \  
tar -xzf /tmp/neo4j.tar.gz -C /usr/local && \  
ln -sf /usr/local/neo4j-community-${NEO4J_VERSION} /usr/local/neo4j  
  
VOLUME /usr/local/neo4j/data  
WORKDIR /usr/local/neo4j  
ENV NEO4J_HOME=/usr/local/neo4j  
ENV PATH=$NEO4J_HOME/bin:$PATH  
ENTRYPOINT ["neo4j", "console"]

