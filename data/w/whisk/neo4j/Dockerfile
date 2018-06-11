FROM whisk/jre:8u45  
  
ENV NEO4J_HOME=/usr/neo4j-community-2.1.8  
RUN curl \  
\--silent \  
\--location \  
\--retry 3 \  
"http://neo4j.com/artifact.php?name=neo4j-community-2.1.8-unix.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $NEO4J_HOME /usr/neo4j  
  
ADD launch.sh /  
  
RUN chmod +x /launch.sh && \  
echo "allow_store_upgrade=true" >> /usr/neo4j/conf/neo4j.properties && \  
sed -i
"s|#org.neo4j.server.webserver.address|org.neo4j.server.webserver.address|g"
/usr/neo4j/conf/neo4j-server.properties  
  
EXPOSE 7474 1337  
VOLUME /usr/neo4j/data/graph.db  
  
## entrypoint  
CMD ["/bin/bash", "-c", "/launch.sh"]  

