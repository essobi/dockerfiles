## Neo4J + spatial  
## based on library/neo4j:3.3  
## Modified from  
FROM library/neo4j:3.3  
MAINTAINER Mahdi Fooladgar, m.fooladgar@ec.iut.ac.ir  
  
# Install neo4j spatial  
WORKDIR /tmp  
RUN wget -q
"https://github.com/neo4j-contrib/spatial/releases/download/0.25.3-neo4j-3.3.1/neo4j-spatial-0.25.3-neo4j-3.3.1-server-
plugin.jar" -O neo4j-spatial-0.25.3-neo4j-3.3.1-server-plugin.jar  
RUN mv neo4j-spatial-0.25.3-neo4j-3.3.1-server-plugin.jar
/var/lib/neo4j/plugins/  
  
WORKDIR /  
  
## entrypoint  
CMD ["neo4j"]  

