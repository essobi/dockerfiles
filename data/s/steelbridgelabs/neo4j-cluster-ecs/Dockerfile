FROM neo4j:3.2-enterprise  
  
RUN apk add --no-cache --quiet curl && \  
mkdir -p /tools && \  
$(cd /tools && curl --fail --silent --show-error --location --remote-name
http://central.maven.org/maven2/com/steelbridgelabs/oss/neo4j-cluster-ecs-
tools/0.0.3/neo4j-cluster-ecs-tools-0.0.3-jar-with-dependencies.jar) && \  
mv /tools/neo4j-cluster-ecs-tools-0.0.3-jar-with-dependencies.jar
/tools/neo4j-cluster-ecs-tools-jar-with-dependencies.jar && \  
apk del curl  
  
COPY start.sh /start.sh  
  
EXPOSE 5000 6000 7000 7473 7474 7687  
ENTRYPOINT ["/start.sh"]  
  
CMD ["cluster"]  

