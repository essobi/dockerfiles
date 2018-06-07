FROM neo4j/neo4j:2.3.2  
# Resolves virtualbox guest additions shared volume problem by moving  
# rrd storage.  
RUN sed -i -e
"s|org.neo4j.server.webadmin.rrdb.location=.*|org.neo4j.server.webadmin.rrdb.location=/tmp/rrd|g"
/var/lib/neo4j/conf/neo4j-server.properties && \  
touch /tmp/rrd  

