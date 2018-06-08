FROM neo4j:3.1  
MAINTAINER samuel.gratzl@datavisyn.io  
  
COPY neo4j-k-shortest-paths-plugin-*.jar /var/lib/neo4j/plugins/  
# register plugin  
RUN echo
dbms.unmanaged_extension_classes=org.caleydo.neo4j.plugins.kshortestpaths=/caleydo
>> /var/lib/neo4j/conf/neo4j.conf

