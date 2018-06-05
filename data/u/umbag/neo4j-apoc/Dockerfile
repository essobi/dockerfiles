FROM neo4j:3.3.2  
LABEL maintainer="Marcel Amsler"  
  
ENV APOC_URI https://github.com/neo4j-contrib/neo4j-apoc-
procedures/releases/download/3.3.0.1/apoc-3.3.0.1-all.jar  
  
RUN wget $APOC_URI && mv apoc-3.3.0.1-all.jar plugins/apoc-3.3.0.1-all.jar  
  
EXPOSE 7474 7473 7687  
CMD ["neo4j"]

