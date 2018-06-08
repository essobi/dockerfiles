#  
# Dockerfile for Cassandra with memory tweaking.  
#  
# VERSION 3.7.0  
FROM cassandra:3.7  
RUN sed -ri -e 's/^#?MAX_HEAP_SIZE=.*$/MAX_HEAP_SIZE="256M"/'
$CASSANDRA_CONFIG/cassandra-env.sh \  
&& sed -ri -e 's/^#?HEAP_NEWSIZE=.*$/HEAP_NEWSIZE="100M"/'
$CASSANDRA_CONFIG/cassandra-env.sh  

