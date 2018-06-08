FROM neo4j:3.2.5  
RUN apk add --update zip unzip && rm -rf /var/cache/apk/*  
  
ADD
https://github.com/neo4j-contrib/m2/blob/master/releases/org/neo4j/neo4j-spatial/0.24.1-neo4j-3.2.5/neo4j-spatial-0.24.1-neo4j-3.2.5-server-
plugin.jar?raw=true /var/lib/neo4j/plugins/neo4j-spatial-server-plugin.jar  
  
EXPOSE 7474  
EXPOSE 7687  
CMD ["neo4j"]  

