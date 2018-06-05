# Adding APOC and the Spatial Library to Official Neo4j Docker Image  
FROM neo4j:latest  
MAINTAINER Clifford Anderson <anderson.clifford@gmail.com>  
  
ENV APOC_URI https://github.com/neo4j-contrib/neo4j-apoc-
procedures/releases/download/3.0.4.1/apoc-3.0.4.1-all.jar  
ENV GIS_URI
https://github.com/neo4j-contrib/m2/blob/master/releases/org/neo4j/neo4j-spatial/0.19-neo4j-3.0.3/neo4j-spatial-0.19-neo4j-3.0.3-server-
plugin.jar?raw=true  
  
RUN mv plugins /plugins \  
&& ln --symbolic /plugins  
  
RUN curl --fail --silent --show-error --location --output apoc-3.0.4.1-all.jar
$APOC_URI \  
&& mv apoc-3.0.4.1-all.jar /plugins  
  
RUN curl --fail --silent --show-error --location --output
neo4j-spatial-0.19-neo4j-3.0.3-server-plugin.jar $GIS_URI \  
&& mv neo4j-spatial-0.19-neo4j-3.0.3-server-plugin.jar /plugins  
  
EXPOSE 7474 7473 7687  
CMD ["neo4j"]  

